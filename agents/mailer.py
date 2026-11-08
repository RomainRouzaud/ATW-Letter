"""
Email sender module for the Veille Tech Agent.
Sends the weekly newsletter as a rich HTML email via SMTP.

Configuration loaded from config/email_config.yaml
SMTP credentials stored in .env:
  EMAIL_SENDER   : sender address (Gmail)
  EMAIL_PASSWORD : Gmail App Password (not the account password!)
"""
import os
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import yaml
import re
import subprocess
from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "email_config.yaml")


def load_email_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        return {}
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def markdown_to_html(md: str) -> str:
    """
    Lightweight Markdown → HTML converter for the newsletter.
    Handles headings, bold, italic, links, horizontal rules, lists, blockquotes.
    """
    lines = md.split("\n")
    html_lines = []
    in_ul = False

    for line in lines:
        # Horizontal rule
        if re.match(r"^---+$", line.strip()):
            if in_ul:
                html_lines.append("</ul>")
                in_ul = False
            html_lines.append('<hr style="border:none;border-top:1px solid #e2e8f0;margin:24px 0">')
            continue

        # Headings
        if line.startswith("#### "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            html_lines.append(f'<h4 style="color:#1e3a5f;margin:16px 0 4px">{_inline(line[5:])}</h4>')
        elif line.startswith("### "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            html_lines.append(f'<h3 style="color:#1e3a5f;margin:24px 0 8px;border-left:4px solid #2563eb;padding-left:12px">{_inline(line[4:])}</h3>')
        elif line.startswith("## "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            html_lines.append(f'<h2 style="color:#0f2d5e;margin:32px 0 12px;font-size:1.25em">{_inline(line[3:])}</h2>')
        elif line.startswith("# "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            html_lines.append(f'<h1 style="color:#0f2d5e;font-size:1.5em;margin:0 0 8px">{_inline(line[2:])}</h1>')

        # Blockquote / warning
        elif line.startswith("> ⚠️") or line.startswith("> "):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            inner = _inline(line.lstrip("> ").strip())
            html_lines.append(
                f'<blockquote style="border-left:4px solid #f59e0b;background:#fffbeb;'
                f'margin:12px 0;padding:10px 16px;border-radius:0 8px 8px 0;color:#92400e">{inner}</blockquote>'
            )

        # Unordered list items
        elif line.startswith("* ") or line.startswith("- "):
            if not in_ul:
                html_lines.append('<ul style="margin:8px 0;padding-left:20px">')
                in_ul = True
            html_lines.append(f'<li style="margin:6px 0;line-height:1.6">{_inline(line[2:])}</li>')

        # Table row
        elif line.startswith("|") and "|" in line[1:]:
            if in_ul: html_lines.append("</ul>"); in_ul = False
            cells = [c.strip() for c in line.strip("|").split("|")]
            # skip separator rows (|---|---|)
            if all(re.match(r"^[-:]+$", c) for c in cells if c):
                continue
            tag = "th" if any(c.startswith("**") for c in cells) else "td"
            row = "".join(f'<{tag} style="padding:8px 12px;border-bottom:1px solid #e2e8f0;text-align:left">{_inline(c)}</{tag}>' for c in cells)
            html_lines.append(f'<tr>{row}</tr>')

        # Blank line
        elif line.strip() == "":
            if in_ul:
                html_lines.append("</ul>")
                in_ul = False
            html_lines.append("")

        # Image block
        elif line.strip().startswith("![") and "](" in line.strip() and line.strip().endswith(")"):
            if in_ul: html_lines.append("</ul>"); in_ul = False
            m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", line.strip())
            if m:
                alt, src = m.group(1), m.group(2)
                html_lines.append(
                    f'<div style="text-align:center;margin:24px 0;">'
                    f'<img src="{src}" alt="{alt}" style="max-width:100%;height:auto;border-radius:8px;border:1px solid #e2e8f0;box-shadow:0 4px 12px rgba(0,0,0,0.08);display:inline-block;">'
                    f'<p style="font-size:12px;color:#64748b;margin-top:8px;font-style:italic;">{alt}</p>'
                    f'</div>'
                )
                continue

        # Normal paragraph
        else:
            if in_ul: html_lines.append("</ul>"); in_ul = False
            if line.strip():
                html_lines.append(f'<p style="margin:8px 0;line-height:1.7;color:#374151">{_inline(line)}</p>')

    if in_ul:
        html_lines.append("</ul>")

    # Wrap table rows in <table>
    body = "\n".join(html_lines)
    body = re.sub(r"(<tr>.*?</tr>\n?)+", lambda m: f'<table style="width:100%;border-collapse:collapse;margin:16px 0">{m.group(0)}</table>', body, flags=re.DOTALL)

    return body


def _inline(text: str) -> str:
    """Apply inline markdown (images, bold, italic, code, links)."""
    # Images ![alt](url) handled before links
    text = re.sub(
        r"!\[([^\]]*)\]\(([^)]+)\)",
        r'<div style="text-align:center;margin:20px 0;"><img src="\2" alt="\1" style="max-width:100%;height:auto;border-radius:8px;border:1px solid #e2e8f0;display:inline-block;"><br><span style="font-size:12px;color:#64748b;font-style:italic;">\1</span></div>',
        text
    )
    # Bold+italic
    text = re.sub(r"\*\*\*(.*?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # Bold
    text = re.sub(r"\*\*(.*?)\*\*", r'<strong style="color:#0f2d5e">\1</strong>', text)
    # Italic
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    # Inline code
    text = re.sub(r"`(.*?)`", r'<code style="background:#f1f5f9;padding:2px 6px;border-radius:4px;font-size:.9em;color:#1e40af">\1</code>', text)
    # Links
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" style="color:#2563eb;text-decoration:none">\1</a>', text)
    return text


def build_html_email(markdown_content: str, subject: str) -> str:
    """Wrap the newsletter content in a professional HTML email template."""
    body = markdown_to_html(markdown_content)
    today = datetime.now().strftime("%d %B %Y")

    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{subject}</title>
</head>
<body style="margin:0;padding:0;background:#f0f4f8;font-family:'Segoe UI',Arial,sans-serif">
  <table width="100%" cellpadding="0" cellspacing="0" style="background:#f0f4f8;padding:32px 0">
    <tr><td align="center">
      <table width="680" cellpadding="0" cellspacing="0" style="max-width:680px;width:100%">

        <!-- HEADER -->
        <tr>
          <td style="background:linear-gradient(135deg,#0f2d5e 0%,#1d4ed8 100%);border-radius:12px 12px 0 0;padding:32px 40px">
            <p style="margin:0;color:#93c5fd;font-size:12px;letter-spacing:2px;text-transform:uppercase">ITGA · Architecture d'Entreprise</p>
            <h1 style="margin:8px 0 4px;color:#ffffff;font-size:24px;font-weight:700">ITGA TechWatch</h1>
            <p style="margin:0;color:#bfdbfe;font-size:14px">Veille hebdomadaire — {today}</p>
          </td>
        </tr>

        <!-- BODY -->
        <tr>
          <td style="background:#ffffff;padding:40px;border-left:1px solid #e2e8f0;border-right:1px solid #e2e8f0">
            {body}
          </td>
        </tr>

        <!-- FOOTER -->
        <tr>
          <td style="background:#1e3a5f;border-radius:0 0 12px 12px;padding:24px 40px;text-align:center">
            <p style="margin:0 0 8px;color:#93c5fd;font-size:12px">
              Rapport généré automatiquement par le système de veille ITGA · 45 sources spécialisées
            </p>
            <p style="margin:0;color:#475569;font-size:11px">
              Ce message est destiné uniquement à son destinataire. Pour vous désabonner, contactez l'expéditeur.
            </p>
          </td>
        </tr>

      </table>
    </td></tr>
  </table>
</body>
</html>"""


def get_password_from_keychain(account_name: str) -> str | None:
    """Retrieve password securely from macOS Keychain."""
    try:
        # -s specifies the service name, -a specifies the account, -w extracts just the password
        cmd = ["security", "find-generic-password", "-s", "ITGA_TechWatch", "-a", account_name, "-w"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def send_newsletter(markdown_content: str) -> bool:
    """
    Send the newsletter email using the config in email_config.yaml.
    Password is securely retrieved from macOS Keychain.
    """
    cfg = load_email_config()

    sender = os.environ.get("EMAIL_SENDER") or cfg.get("sender")
    recipients = cfg.get("recipients", [])
    subject = cfg.get("subject", "ITGA TechWatch")
    smtp_host = cfg.get("smtp_host", "smtp.gmail.com")
    smtp_port = int(cfg.get("smtp_port", 587))

    if not sender:
        print("[Email] EMAIL_SENDER manquant dans .env")
        return False
        
    # Securely fetch the password from the macOS Keychain
    password = get_password_from_keychain(sender)
    if not password:
        # Fallback to .env just in case, but warn
        password = os.environ.get("EMAIL_PASSWORD") or cfg.get("password")
        if not password:
            print(f"[Email] ❌ Mot de passe introuvable dans le Trousseau macOS pour {sender}.")
            print("Pour l'ajouter : security add-generic-password -s 'ITGA_TechWatch' -a 'VOTRE_EMAIL' -W")
            return False

    if not recipients:
        print("[Email] Aucun destinataire configuré dans email_config.yaml")
        return False

    # Build message
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"ITGA TechWatch <{sender}>"
    msg["To"] = ", ".join(recipients)

    html_content = build_html_email(markdown_content, subject)
    msg.attach(MIMEText(markdown_content, "plain", "utf-8"))
    msg.attach(MIMEText(html_content, "html", "utf-8"))

    # Send
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(sender, password)
            server.sendmail(sender, recipients, msg.as_string())
        print(f"[Email] ✅ Newsletter envoyée à : {', '.join(recipients)}")
        return True
    except Exception as e:
        print(f"[Email] ❌ Erreur d'envoi : {e}")
        return False
