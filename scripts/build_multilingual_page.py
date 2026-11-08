#!/usr/bin/env python3
"""
ITGA Enterprise TechWatch — Multilingual Newsletter Publisher
Generates an interactive, responsive HTML page with a language selector
(FR, EN, NL, PL, IT, TR, UK) and browser-language auto-detection.

Can be run standalone or imported into main.py (run_weekly).
"""
import os
import sys
import re
import glob
import time
from pathlib import Path

# Add project root to path for imports
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from agents.llm_client import LLMClient

NEWSLETTER_DIR = PROJECT_ROOT / "data" / "newsletters"
ARTIFACT_DIR = Path("/Users/romainrouzaud/.gemini/antigravity/brain/60fa75f4-8d8d-4b7d-8070-173e42aa4a10")

LANGUAGES = [
    {"code": "fr", "name": "Français", "flag": "🇫🇷"},
    {"code": "en", "name": "English", "flag": "🇬🇧"},
    {"code": "nl", "name": "Nederlands", "flag": "🇳🇱"},
    {"code": "pl", "name": "Polski", "flag": "🇵🇱"},
    {"code": "it", "name": "Italiano", "flag": "🇮🇹"},
    {"code": "tr", "name": "Türkçe", "flag": "🇹🇷"},
    {"code": "uk", "name": "Українська", "flag": "🇺🇦"},
]


# ─────────────────────────────────────────────
# Markdown to HTML Parser
# ─────────────────────────────────────────────
def inline_format(text: str) -> str:
    """Format inline markdown elements: bold, italic, code, links."""
    text = re.sub(r"\*\*\*(.*?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.*?)\*\*", r'<strong class="font-bold text-[var(--foreground,#0f172a)]">\1</strong>', text)
    text = re.sub(r"\*(.*?)\*", r'<em class="italic text-[var(--muted-foreground,#475569)]">\1</em>', text)
    text = re.sub(r"`(.*?)`", r'<code class="px-1.5 py-0.5 rounded text-xs font-mono bg-[var(--muted,#f1f5f9)] text-blue-600 dark:text-blue-400 font-semibold">\1</code>', text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener noreferrer" class="text-blue-600 dark:text-blue-400 font-medium hover:underline inline-flex items-center gap-0.5">\1 <span class="text-xs opacity-70">↗</span></a>', text)
    return text


def parse_markdown(md_text: str) -> str:
    """Parses markdown text into clean, modern Tailwind-styled HTML."""
    lines = md_text.split("\n")
    html_lines = []
    in_ul = False
    in_table = False

    for line in lines:
        sline = line.strip()

        # Close list if non-list line
        is_list_item = sline.startswith("* ") or sline.startswith("- ")
        if in_ul and not is_list_item:
            html_lines.append("</ul>")
            in_ul = False

        # Table handling
        if sline.startswith("|") and sline.endswith("|"):
            # Table separator row (|---|---|)
            if re.match(r"^\|(\s*:?-+:?\s*\|)+$", sline):
                continue
            cells = [c.strip() for c in sline.split("|")[1:-1]]
            if not in_table:
                in_table = True
                html_lines.append('<div class="my-6 overflow-x-auto rounded-xl border border-[var(--border,#e2e8f0)] shadow-xs"><table class="w-full text-left border-collapse text-sm">')
                html_lines.append('<thead class="bg-[var(--muted,#f1f5f9)] border-b border-[var(--border,#e2e8f0)]"><tr>')
                for c in cells:
                    html_lines.append(f'<th class="px-4 py-3 font-semibold text-[var(--foreground,#0f172a)]">{inline_format(c)}</th>')
                html_lines.append('</tr></thead><tbody class="divide-y divide-[var(--border,#e2e8f0)]">')
            else:
                html_lines.append('<tr class="hover:bg-[var(--accent,#f8fafc)] transition-colors">')
                for c in cells:
                    html_lines.append(f'<td class="px-4 py-3 text-[var(--foreground,#334155)]">{inline_format(c)}</td>')
                html_lines.append('</tr>')
            continue
        elif in_table:
            html_lines.append('</tbody></table></div>')
            in_table = False

        # Horizontal Rule
        if re.match(r"^---+$", sline):
            html_lines.append('<hr class="my-8 border-t border-[var(--border,#e2e8f0)]">')
            continue

        # Blockquote
        if sline.startswith("> "):
            html_lines.append(f'<blockquote class="my-4 pl-4 border-l-4 border-blue-500 bg-blue-50/50 dark:bg-blue-950/20 py-2 rounded-r-lg text-sm text-[var(--foreground,#334155)] italic">{inline_format(sline[2:])}</blockquote>')
            continue

        # H1
        if sline.startswith("# "):
            html_lines.append(f'<div class="mb-6 pb-4 border-b border-[var(--border,#e2e8f0)]"><h1 class="text-2xl sm:text-3xl font-extrabold text-[var(--foreground,#0f172a)] tracking-tight">{inline_format(sline[2:])}</h1></div>')
            continue

        # H2
        if sline.startswith("## "):
            html_lines.append(f'<div class="mt-10 mb-4 pt-4 border-t border-[var(--border,#e2e8f0)] first:border-t-0"><h2 class="text-xl sm:text-2xl font-bold text-[var(--foreground,#0f172a)] flex items-center gap-2">{inline_format(sline[3:])}</h2></div>')
            continue

        # H3
        if sline.startswith("### "):
            html_lines.append(f'<h3 class="text-base sm:text-lg font-bold text-[var(--foreground,#0f172a)] mt-6 mb-2 pl-3 border-l-4 border-blue-600 dark:border-blue-500">{inline_format(sline[4:])}</h3>')
            continue

        # H4
        if sline.startswith("#### "):
            html_lines.append(f'<h4 class="text-sm sm:text-base font-semibold text-[var(--foreground,#0f172a)] mt-4 mb-1">{inline_format(sline[5:])}</h4>')
            continue

        # Images
        if sline.startswith("![") and "](" in sline and sline.endswith(")"):
            m = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)$", sline)
            if m:
                alt, src = m.group(1), m.group(2)
                html_lines.append(f'''
                <div class="my-6 p-4 rounded-xl bg-[var(--card,#ffffff)] border border-[var(--border,#e2e8f0)] shadow-sm text-center">
                    <img src="{src}" alt="{alt}" loading="lazy" class="max-w-full h-auto mx-auto rounded-lg border border-[var(--border,#e2e8f0)] shadow-sm hover:scale-[1.01] transition-transform">
                    <p class="mt-3 text-xs text-[var(--muted-foreground,#64748b)] italic font-medium">{alt}</p>
                </div>
                ''')
            continue

        # Unordered list items
        if is_list_item:
            if not in_ul:
                html_lines.append('<ul class="space-y-2 my-4 pl-5 list-disc text-[var(--foreground,#334155)]">')
                in_ul = True
            html_lines.append(f'<li class="leading-relaxed text-sm sm:text-base">{inline_format(sline[2:])}</li>')
            continue

        # Numbered items (e.g. 1. Pilot...)
        m_num = re.match(r"^(\d+)\.\s+(.*)$", sline)
        if m_num:
            num, rest = m_num.group(1), m_num.group(2)
            html_lines.append(f'''
            <div class="mt-4 mb-2 flex items-start gap-3">
                <span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-blue-100 text-blue-700 dark:bg-blue-900/60 dark:text-blue-300 font-bold text-xs shrink-0 mt-0.5">{num}</span>
                <div class="text-sm sm:text-base text-[var(--foreground,#334155)] font-medium leading-relaxed">{inline_format(rest)}</div>
            </div>
            ''')
            continue

        # Empty lines
        if not sline:
            continue

        # Paragraph
        html_lines.append(f'<p class="my-3 leading-relaxed text-sm sm:text-base text-[var(--foreground,#334155)] opacity-95">{inline_format(sline)}</p>')

    if in_ul:
        html_lines.append("</ul>")
    if in_table:
        html_lines.append('</tbody></table></div>')

    return "\n".join(html_lines)


# ─────────────────────────────────────────────
# Translation Engine
# ─────────────────────────────────────────────
def clean_translated_text(text: str) -> str:
    """Cleans up raw LLM output, removing any introductory chatter or code fences."""
    if not text:
        return ""
    cleaned = text.strip()
    if cleaned.startswith("```markdown"):
        cleaned = cleaned[11:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()

    # Strip conversational lead-in if model added one
    lines = cleaned.split("\n")
    if len(lines) > 2 and lines[0].lower().startswith(("here is", "here's", "voici", "below is")):
        # Skip until first header or rule
        start_idx = 1
        while start_idx < len(lines) and not (lines[start_idx].startswith("#") or lines[start_idx].startswith("---")):
            start_idx += 1
        cleaned = "\n".join(lines[start_idx:]).strip()

    return cleaned


def chunk_markdown_by_sections(md_text: str, max_chunk_lines: int = 220) -> list[str]:
    """Splits markdown into logical chunks on major headers to avoid LLM token truncation."""
    sections = re.split(r"\n(?=## )", md_text)
    chunks = []
    current_chunk = []
    current_lines = 0

    for sec in sections:
        sec_lines = sec.count("\n") + 1
        if current_lines + sec_lines > max_chunk_lines and current_chunk:
            chunks.append("\n".join(current_chunk))
            current_chunk = [sec]
            current_lines = sec_lines
        else:
            current_chunk.append(sec)
            current_lines += sec_lines

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks


def translate_newsletter_content(md_content: str, target_lang: dict, client: LLMClient) -> str:
    """Translates newsletter markdown chunk-by-chunk using LLMClient."""
    code = target_lang["code"]
    name = target_lang["name"]
    print(f"  [Multilingual] Traduction en {name} ({code})...")

    chunks = chunk_markdown_by_sections(md_content, max_chunk_lines=220)
    translated_chunks = []

    for idx, chunk in enumerate(chunks, 1):
        prompt = f"""Tu es un traducteur technique bilingue expert en Architecture d'Entreprise, Cloud, Banques, Systèmes Distribués et IA.
Traduis fidèlement le passage Markdown suivant en {name} ({code}).

Règles impératives :
1. Conserve STRICTEMENT toute la syntaxe Markdown (titres #, ##, ###, listes, tableaux, balises, sauts de ligne).
2. Conserve STRICTEMENT toutes les URLs d'images ![alt](URL) et les liens [texte](URL) sans altérer les adresses URLs.
3. Conserve les termes techniques IT et bancaires usuels en anglais (ex: Serverless, Zero Trust, GraphRAG, SRE, FinOps, Event-Driven, Covenants, Due Diligence, Next Best Action, Deep XVA).
4. Fournis une traduction fluide, percutante et de très haut niveau pour des dirigeants IT / Architectes d'Entreprise.
5. Ne donne AUCUN texte d'introduction ni de conclusion. Réponds STRICTEMENT et UNIQUEMENT avec le contenu Markdown traduit.

Texte à traduire :
{chunk}
"""
        translated = client.generate(prompt)
        if translated:
            cleaned = clean_translated_text(translated)
            translated_chunks.append(cleaned)
        else:
            print(f"    ⚠️ Avertissement : échec traduction chunk {idx}/{len(chunks)}, conservation de la version d'origine.")
            translated_chunks.append(chunk)
        time.sleep(1)

    return "\n\n".join(translated_chunks)


def ensure_language_versions(base_file: Path, client: LLMClient | None = None, translate: bool = True) -> dict[str, str]:
    """
    Ensures markdown files exist for each of the 7 languages for the given newsletter.
    If a language file is missing and translate=True, it is generated via LLM.
    Returns: dict mapping lang_code -> markdown content string.
    """
    with open(base_file, "r", encoding="utf-8") as f:
        french_content = f.read()

    # Extract date from filename (e.g. newsletter_2026-11-08.md -> 2026-11-08)
    m = re.search(r"newsletter_(\d{4}-\d{2}-\d{2})", base_file.name)
    date_str = m.group(1) if m else "latest"

    # Always ensure _fr.md exists
    fr_file = NEWSLETTER_DIR / f"newsletter_{date_str}_fr.md"
    if not fr_file.exists():
        with open(fr_file, "w", encoding="utf-8") as f:
            f.write(french_content)

    results = {"fr": french_content}

    # Process other languages
    for lang in LANGUAGES:
        code = lang["code"]
        if code == "fr":
            continue

        target_file = NEWSLETTER_DIR / f"newsletter_{date_str}_{code}.md"
        if target_file.exists():
            with open(target_file, "r", encoding="utf-8") as f:
                results[code] = f.read()
        elif translate:
            if client is None:
                client = LLMClient()
            translated = translate_newsletter_content(french_content, lang, client)
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(translated)
            results[code] = translated
            print(f"  ✓ Sauvegardé : {target_file.name}")
        else:
            # Fallback when translation is disabled: check previous translated versions or use base content
            prev_candidates = sorted(NEWSLETTER_DIR.glob(f"newsletter_*_{code}.md"), reverse=True)
            if prev_candidates:
                with open(prev_candidates[0], "r", encoding="utf-8") as f:
                    results[code] = f.read()
            else:
                results[code] = french_content

    return results


# ─────────────────────────────────────────────
# HTML Builder
# ─────────────────────────────────────────────
def build_html_document(lang_contents: dict[str, str], date_str: str = "") -> str:
    """Builds the comprehensive, interactive HTML document from language contents."""
    select_options_html = []
    pill_buttons_html = []
    tab_contents_html = []

    # Format human-friendly date (e.g. 2026-11-08 -> 08 Novembre 2026)
    display_date = date_str
    if re.match(r"^\d{4}-\d{2}-\d{2}$", date_str):
        parts = date_str.split("-")
        months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        m_idx = int(parts[1]) - 1
        if 0 <= m_idx < 12:
            display_date = f"{parts[2]} {months[m_idx]} {parts[0]}"

    for i, lang in enumerate(LANGUAGES):
        code = lang["code"]
        name = lang["name"]
        flag = lang["flag"]
        content_md = lang_contents.get(code, f"# Document non trouvé pour {name}")

        parsed_html = parse_markdown(content_md)

        # Initial active state (FR default, will be overridden by client-side auto-detect JS)
        is_first = (i == 0)
        content_hidden = "" if is_first else "hidden"
        pill_active_class = "bg-blue-600 text-white font-semibold shadow-xs" if is_first else "text-[var(--muted-foreground,#64748b)] hover:bg-[var(--accent,#f1f5f9)] hover:text-[var(--foreground,#0f172a)]"

        # Select option
        select_options_html.append(f'<option value="{code}">{flag} {name}</option>')

        # Quick Pill button
        pill_buttons_html.append(f'''
        <button onclick="switchTab('{code}')" id="pill-{code}" data-lang="{code}" class="tab-btn px-2.5 py-1 rounded-lg text-xs transition-all duration-150 flex items-center gap-1.5 cursor-pointer {pill_active_class}">
            <span>{flag}</span>
            <span class="font-medium">{code.upper()}</span>
        </button>
        ''')

        # Content container
        tab_contents_html.append(f'''
        <div id="tab-{code}" class="tab-pane {content_hidden} animate-fadeIn">
            <div class="newsletter-body max-w-4xl mx-auto">
                {parsed_html}
            </div>
        </div>
        ''')

    return f'''<!DOCTYPE html>
<html lang="fr" class="h-full">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise TechWatch — Multilingual Edition ({display_date})</title>
    <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
    <style>
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        .animate-fadeIn {{
            animation: fadeIn 0.2s ease-out forwards;
        }}
    </style>
</head>
<body class="bg-[var(--background,#f8fafc)] text-[var(--foreground,#0f172a)] antialiased min-h-full flex flex-col font-sans">

    <!-- Top Sticky Header -->
    <header class="sticky top-0 z-50 bg-[var(--card,#ffffff)]/95 backdrop-blur-md border-b border-[var(--border,#e2e8f0)] shadow-xs">
        <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-16 gap-4">
                
                <!-- Brand / Metadata -->
                <div class="flex items-center gap-3 shrink-0">
                    <span class="text-2xl">🏛️</span>
                    <div>
                        <div class="flex items-center gap-2">
                            <h1 class="font-bold text-sm sm:text-base text-[var(--foreground,#0f172a)] leading-tight">Enterprise TechWatch</h1>
                            <span class="px-2 py-0.5 rounded-full text-[11px] font-semibold bg-blue-100 text-blue-700 dark:bg-blue-900/60 dark:text-blue-300">Edition Hebdo</span>
                        </div>
                        <p class="text-xs text-[var(--muted-foreground,#64748b)] hidden sm:block">Architecture d'Entreprise SI • {display_date}</p>
                    </div>
                </div>

                <!-- Central Control: Language Dropdown Selector + Auto-detect Badge -->
                <div class="flex items-center gap-3">
                    <div class="flex items-center gap-2 bg-[var(--muted,#f1f5f9)] p-1 rounded-xl border border-[var(--border,#e2e8f0)]">
                        
                        <!-- Dropdown Select -->
                        <div class="relative inline-flex items-center">
                            <span class="absolute left-3 text-sm pointer-events-none" id="selected-flag">🇫🇷</span>
                            <select id="lang-select" onchange="switchTab(this.value)" aria-label="Choisir la langue de la newsletter"
                                class="appearance-none pl-8 pr-8 py-1.5 text-xs sm:text-sm font-semibold rounded-lg bg-[var(--card,#ffffff)] border border-[var(--border,#cbd5e1)] text-[var(--foreground,#0f172a)] shadow-xs hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all cursor-pointer">
                                {''.join(select_options_html)}
                            </select>
                            <svg class="w-3.5 h-3.5 absolute right-2.5 pointer-events-none text-[var(--muted-foreground,#64748b)]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </div>

                        <!-- Quick Pills Bar (Desktop shortcut) -->
                        <div class="hidden lg:flex items-center gap-1 border-l border-[var(--border,#cbd5e1)] pl-2">
                            {''.join(pill_buttons_html)}
                        </div>
                    </div>

                    <!-- Auto-detection badge -->
                    <div id="browser-detected-badge" class="hidden sm:inline-flex items-center gap-1.5 px-2.5 py-1 rounded-lg text-[11px] font-medium bg-emerald-50 text-emerald-700 dark:bg-emerald-950/60 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800" title="Langue présélectionnée automatiquement d'après votre navigateur">
                        <span class="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse"></span>
                        <span id="detected-lang-label">Auto-détecté</span>
                    </div>
                </div>

                <!-- Actions: Print / PDF -->
                <div class="flex items-center gap-2">
                    <button onclick="window.print()" class="px-3 py-1.5 rounded-lg text-xs font-medium border border-[var(--border,#e2e8f0)] bg-[var(--card,#ffffff)] text-[var(--foreground,#0f172a)] hover:bg-[var(--accent,#f1f5f9)] transition-colors hidden sm:flex items-center gap-1.5 shadow-2xs cursor-pointer">
                        <span>🖨️</span>
                        <span>Imprimer</span>
                    </button>
                </div>
            </div>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="grow max-w-5xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-12">
        <div class="bg-[var(--card,#ffffff)] border border-[var(--border,#e2e8f0)] rounded-2xl p-6 sm:p-10 shadow-sm">
            {''.join(tab_contents_html)}
        </div>
    </main>

    <!-- Footer -->
    <footer class="mt-auto py-6 border-t border-[var(--border,#e2e8f0)] bg-[var(--card,#ffffff)]/50 text-center text-xs text-[var(--muted-foreground,#64748b)]">
        <div class="max-w-6xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-2">
            <p>Système multi-agents autonome de veille stratégique SI • Banques, Assurance, Énergie & Systèmes Critiques</p>
            <p class="font-medium">7 versions : FR • EN • NL • PL • IT • TR • UK</p>
        </div>
    </footer>

    <!-- Interactive Dropdown & Auto-detection Script -->
    <script>
        const SUPPORTED_LANGS = ['fr', 'en', 'nl', 'pl', 'it', 'tr', 'uk'];
        const LANG_METADATA = {{
            'fr': {{ name: 'Français', flag: '🇫🇷' }},
            'en': {{ name: 'English', flag: '🇬🇧' }},
            'nl': {{ name: 'Nederlands', flag: '🇳🇱' }},
            'pl': {{ name: 'Polski', flag: '🇵🇱' }},
            'it': {{ name: 'Italiano', flag: '🇮🇹' }},
            'tr': {{ name: 'Türkçe', flag: '🇹🇷' }},
            'uk': {{ name: 'Українська', flag: '🇺🇦' }}
        }};

        function detectBrowserLanguage() {{
            const browserLangs = navigator.languages || [navigator.language || navigator.userLanguage || ''];
            for (let i = 0; i < browserLangs.length; i++) {{
                const raw = browserLangs[i];
                if (!raw) continue;
                const code = raw.toLowerCase().split('-')[0];
                if (SUPPORTED_LANGS.includes(code)) {{
                    return code;
                }}
            }}
            return 'fr';
        }}

        function switchTab(langCode, isAuto = false) {{
            if (!SUPPORTED_LANGS.includes(langCode)) {{
                langCode = 'fr';
            }}

            // 1. Hide all tab panes
            document.querySelectorAll('.tab-pane').forEach(function(pane) {{
                pane.classList.add('hidden');
            }});

            // 2. Show active pane
            const activePane = document.getElementById('tab-' + langCode);
            if (activePane) {{
                activePane.classList.remove('hidden');
            }}

            // 3. Sync select dropdown
            const selectEl = document.getElementById('lang-select');
            if (selectEl && selectEl.value !== langCode) {{
                selectEl.value = langCode;
            }}

            // 4. Update flag icon inside dropdown
            const flagEl = document.getElementById('selected-flag');
            if (flagEl && LANG_METADATA[langCode]) {{
                flagEl.textContent = LANG_METADATA[langCode].flag;
            }}

            // 5. Update quick pill buttons
            document.querySelectorAll('.tab-btn').forEach(function(btn) {{
                const bCode = btn.getAttribute('data-lang');
                if (bCode === langCode) {{
                    btn.className = 'tab-btn px-2.5 py-1 rounded-lg text-xs font-semibold bg-blue-600 text-white shadow-xs cursor-pointer';
                }} else {{
                    btn.className = 'tab-btn px-2.5 py-1 rounded-lg text-xs font-medium text-[var(--muted-foreground,#64748b)] hover:bg-[var(--accent,#f1f5f9)] hover:text-[var(--foreground,#0f172a)] transition-colors cursor-pointer';
                }}
            }});

            // 6. Update document lang attribute
            document.documentElement.lang = langCode;

            // 7. Store choice unless it was first-time auto-detected
            if (!isAuto) {{
                try {{
                    localStorage.setItem('techwatch_lang', langCode);
                    window.location.hash = langCode;
                }} catch(e) {{}}
            }}
        }}

        window.addEventListener('DOMContentLoaded', function() {{
            const hash = window.location.hash.replace('#', '').toLowerCase();
            let stored = null;
            try {{ stored = localStorage.getItem('techwatch_lang'); }} catch(e) {{}}

            let selectedLang = 'fr';
            let wasAutoDetected = false;

            if (SUPPORTED_LANGS.includes(hash)) {{
                selectedLang = hash;
            }} else if (SUPPORTED_LANGS.includes(stored)) {{
                selectedLang = stored;
            }} else {{
                selectedLang = detectBrowserLanguage();
                wasAutoDetected = true;
            }}

            switchTab(selectedLang, wasAutoDetected);

            if (wasAutoDetected) {{
                const badge = document.getElementById('browser-detected-badge');
                const label = document.getElementById('detected-lang-label');
                if (badge && label && LANG_METADATA[selectedLang]) {{
                    label.textContent = 'Navigateur : ' + LANG_METADATA[selectedLang].flag + ' ' + LANG_METADATA[selectedLang].name;
                    badge.classList.remove('hidden');
                }}
            }}
        }});
    </script>
</body>
</html>
'''


# ─────────────────────────────────────────────
# Main Publication Pipeline Function
# ─────────────────────────────────────────────
def generate_multilingual_publication(base_filepath: str | Path | None = None, translate: bool = True) -> dict[str, str]:
    """
    Main entry point for publishing the multilingual newsletter.
    - Resolves base newsletter markdown file (defaults to latest in data/newsletters/)
    - Translates or loads versions for the 7 supported languages
    - Generates interactive HTML document
    - Saves to project data/newsletters/ and artifact directory
    Returns: dict of generated paths {'project_html': ..., 'artifact_html': ..., 'dated_html': ...}
    """
    if base_filepath:
        target_file = Path(base_filepath)
    else:
        # Find latest base newsletter (excluding language-specific files)
        candidates = sorted(
            [Path(p) for p in glob.glob(str(NEWSLETTER_DIR / "newsletter_[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))],
            key=lambda p: p.stat().st_mtime,
            reverse=True
        )
        if not candidates:
            print("Aucune newsletter trouvée dans data/newsletters/.")
            return {}
        target_file = candidates[0]

    print(f"[Multilingual] Traitement de la newsletter : {target_file.name}")

    m = re.search(r"newsletter_(\d{4}-\d{2}-\d{2})", target_file.name)
    date_str = m.group(1) if m else time.strftime("%Y-%m-%d")

    # Step 1: Ensure language versions
    client = LLMClient() if translate else None
    lang_contents = ensure_language_versions(target_file, client=client, translate=translate)

    # Step 2: Build HTML
    html_content = build_html_document(lang_contents, date_str=date_str)

    # Step 3: Save outputs
    # 3a. Main project entrypoint
    proj_out = NEWSLETTER_DIR / "multilingual_newsletter.html"
    with open(proj_out, "w", encoding="utf-8") as f:
        f.write(html_content)

    # 3b. Dated archive HTML
    dated_out = NEWSLETTER_DIR / f"newsletter_{date_str}_multilingual.html"
    with open(dated_out, "w", encoding="utf-8") as f:
        f.write(html_content)

    # 3c. Artifact directory for Antigravity UI
    artifact_out = ARTIFACT_DIR / "multilingual_newsletter.html"
    try:
        ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
        with open(artifact_out, "w", encoding="utf-8") as f:
            f.write(html_content)
    except Exception as e:
        print(f"  (Note: sauvegarde artifact omise : {e})")

    print(f"  ✓ Page multilingue enregistrée : {proj_out} ({len(html_content):,} octets)")
    return {
        "project_html": str(proj_out),
        "dated_html": str(dated_out),
        "artifact_html": str(artifact_out),
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Générateur de Page Multilingue ITGA TechWatch")
    parser.add_argument("--file", "-f", help="Chemin vers le fichier newsletter .md", default=None)
    parser.add_argument("--no-translate", action="store_true", help="Ne pas traduire les langues manquantes via LLM")
    args = parser.parse_args()

    generate_multilingual_publication(base_filepath=args.file, translate=not args.no_translate)
