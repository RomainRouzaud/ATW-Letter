#!/usr/bin/env python3
"""
Interactive configuration wizard for the Veille Tech Agent.
Run this script to choose your LLM provider and set your API keys.

Usage:
    python configure.py
"""
import os
import sys
import yaml
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config" / "llm_config.yaml"
ENV_PATH = Path(__file__).parent / ".env"

# ─────────────────────────────────────────────
# Console helpers
# ─────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
CYAN    = "\033[96m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
RED     = "\033[91m"
MAGENTA = "\033[95m"
DIM     = "\033[2m"


def banner():
    print(f"""
{CYAN}{BOLD}╔══════════════════════════════════════════════════════╗
║      🔧  Veille Tech Agent — Configuration LLM       ║
╚══════════════════════════════════════════════════════╝{RESET}
""")


def section(title: str):
    print(f"\n{MAGENTA}{BOLD}── {title} ──{RESET}")


def prompt(msg: str, default: str = "") -> str:
    hint = f" [{DIM}{default}{RESET}]" if default else ""
    value = input(f"  {BOLD}{msg}{RESET}{hint} : ").strip()
    return value if value else default


def choose(options: list[dict]) -> dict:
    """Display a numbered menu and return the chosen option dict."""
    for i, opt in enumerate(options, 1):
        tag = f"  {CYAN}{i}.{RESET} {BOLD}{opt['label']}{RESET}"
        if opt.get("desc"):
            tag += f"\n     {DIM}{opt['desc']}{RESET}"
        print(tag)
    while True:
        raw = input(f"\n  {BOLD}Votre choix (1-{len(options)}) :{RESET} ").strip()
        if raw.isdigit() and 1 <= int(raw) <= len(options):
            return options[int(raw) - 1]
        print(f"  {RED}Entrée invalide, réessayez.{RESET}")


def update_env(key: str, value: str):
    """Update or insert a key=value line in .env, preserving other lines."""
    lines = []
    found = False
    if ENV_PATH.exists():
        with open(ENV_PATH, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith(f"{key}=") or line.startswith(f"{key} ="):
                lines[i] = f'{key}="{value}"\n'
                found = True
                break
    if not found:
        lines.append(f'{key}="{value}"\n')
    with open(ENV_PATH, "w") as f:
        f.writelines(lines)


def save_llm_config(cfg: dict):
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        yaml.dump(cfg, f, allow_unicode=True, default_flow_style=False)
    print(f"\n  {GREEN}✓ Configuration sauvegardée dans {CONFIG_PATH}{RESET}")


def load_current_config() -> dict:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f) or {}
    return {}


# ─────────────────────────────────────────────
# Provider configurators
# ─────────────────────────────────────────────
def configure_mistral(cfg: dict):
    section("Configuration Mistral AI")
    print(f"  {DIM}Obtenez votre clé sur https://console.mistral.ai/api-keys/{RESET}\n")

    models = [
        {"label": "mistral-small-latest",   "desc": "Rapide, économique et très performant — recommandé"},
        {"label": "mistral-large-latest",   "desc": "Modèle de pointe Mistral (raisonnement complexe)"},
        {"label": "codestral-latest",       "desc": "Spécialisé génération de code et architecture"},
        {"label": "open-mistral-nemo",      "desc": "Modèle 12B multilingue ultra-rapide"},
    ]
    print("  Choisissez le modèle Mistral :")
    chosen_model = choose(models)

    api_key = prompt("Clé API Mistral", default=os.environ.get("MISTRAL_API_KEY", ""))
    if api_key:
        update_env("MISTRAL_API_KEY", api_key)

    cfg.update({
        "provider": "mistral",
        "model": chosen_model["label"],
    })
    for k in ["base_url", "project_id"]:
        cfg.pop(k, None)


def configure_gemini(cfg: dict):
    section("Configuration Google Gemini")
    print(f"  {DIM}Obtenez votre clé sur https://aistudio.google.com/apikey{RESET}\n")

    models = [
        {"label": "gemini-3.1-flash-lite",   "desc": "Ultra rapide, haute disponibilité Free Tier — recommandé"},
        {"label": "gemini-flash-lite-latest", "desc": "Dernière version Flash Lite"},
        {"label": "gemini-3.8-flash",        "desc": "Modèle standard haute performance"},
    ]
    print("  Choisissez le modèle Gemini :")
    chosen_model = choose(models)

    api_key = prompt("Clé API Gemini", default=os.environ.get("GEMINI_API_KEY", ""))
    if api_key:
        update_env("GEMINI_API_KEY", api_key)

    cfg.update({
        "provider": "gemini",
        "model": chosen_model["label"],
    })
    # Remove irrelevant keys
    for k in ["base_url", "project_id"]:
        cfg.pop(k, None)


def configure_ollama(cfg: dict):
    section("Configuration Ollama (Local)")
    print(f"  {DIM}Installez Ollama sur https://ollama.com et lancez : ollama serve{RESET}\n")

    models = [
        {"label": "gemma3:27b",     "desc": "Google Gemma 3 27B — excellent en français"},
        {"label": "gemma3:12b",     "desc": "Google Gemma 3 12B — plus léger"},
        {"label": "llama3.3:70b",   "desc": "Meta Llama 3.3 70B"},
        {"label": "mistral:7b",     "desc": "Mistral 7B — très rapide"},
        {"label": "qwen2.5:32b",    "desc": "Qwen 2.5 32B"},
    ]
    print("  Choisissez le modèle Ollama :")
    chosen_model = choose(models)
    custom = prompt("Ou entrez un nom de modèle personnalisé (laisser vide pour garder le choix)")
    model_name = custom if custom else chosen_model["label"]

    base_url = prompt("URL Ollama", default=cfg.get("base_url", "http://localhost:11434"))

    cfg.update({
        "provider": "ollama",
        "model": model_name,
        "base_url": base_url,
    })
    for k in ["project_id"]:
        cfg.pop(k, None)


def configure_watsonx(cfg: dict):
    section("Configuration IBM WatsonX (BAM)")
    print(f"  {DIM}Documentation : https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-api.html{RESET}\n")

    models = [
        {"label": "ibm/granite-3-3-8b-instruct",      "desc": "IBM Granite 3.3 8B — léger et rapide"},
        {"label": "ibm/granite-3-2-8b-instruct",      "desc": "IBM Granite 3.2 8B"},
        {"label": "ibm/granite-34b-code-instruct",    "desc": "IBM Granite 34B Code"},
        {"label": "meta-llama/llama-3-70b-instruct",  "desc": "Meta Llama 3 70B via WatsonX"},
        {"label": "mistralai/mistral-large",           "desc": "Mistral Large via WatsonX"},
    ]
    print("  Choisissez le modèle WatsonX :")
    chosen_model = choose(models)

    api_key = prompt("Clé API IBM Cloud (ibmcloud_api_key)", default=os.environ.get("WATSONX_API_KEY", ""))
    project_id = prompt("WatsonX Project ID", default=os.environ.get("WATSONX_PROJECT_ID", ""))
    base_url = prompt(
        "Endpoint WatsonX",
        default=cfg.get("base_url", "https://eu-de.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29")
    )

    if api_key:
        update_env("WATSONX_API_KEY", api_key)
    if project_id:
        update_env("WATSONX_PROJECT_ID", project_id)

    cfg.update({
        "provider": "watsonx",
        "model": chosen_model["label"],
        "base_url": base_url,
        "project_id": project_id,
    })


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────
def main():
    banner()

    # Show current config
    current = load_current_config()
    if current:
        cur_provider = current.get("provider", "?")
        cur_model = current.get("model", "?")
        print(f"  Configuration actuelle : {CYAN}{cur_provider}{RESET} / {BOLD}{cur_model}{RESET}")
    else:
        print(f"  {YELLOW}Aucune configuration existante.{RESET}")

    section("Choisissez votre fournisseur LLM")

    providers = [
        {
            "label": "Mistral AI API",
            "desc":  "🇫🇷 Cloud — Modèles français de pointe (Mistral Small, Large, Codestral - https://console.mistral.ai)",
            "key":   "mistral",
        },
        {
            "label": "Google Gemini API",
            "desc":  "☁️  Cloud — Nécessite une clé API Google (https://aistudio.google.com)",
            "key":   "gemini",
        },
        {
            "label": "Ollama (Local / On-Premise)",
            "desc":  "🏠 Local — Modèles open-source tournant en local (Gemma, Llama, Mistral…)",
            "key":   "ollama",
        },
        {
            "label": "IBM WatsonX / BAM",
            "desc":  "🏦 Enterprise — Modèles IBM Granite et autres via WatsonX.ai",
            "key":   "watsonx",
        },
    ]

    chosen = choose(providers)
    cfg = dict(current)  # start from existing config

    if chosen["key"] == "mistral":
        configure_mistral(cfg)
    elif chosen["key"] == "gemini":
        configure_gemini(cfg)
    elif chosen["key"] == "ollama":
        configure_ollama(cfg)
    elif chosen["key"] == "watsonx":
        configure_watsonx(cfg)

    save_llm_config(cfg)

    print(f"""
{GREEN}{BOLD}✅ Configuration terminée !{RESET}
  Provider : {CYAN}{cfg['provider']}{RESET}
  Modèle   : {BOLD}{cfg['model']}{RESET}

  Pour lancer le job quotidien :
    {DIM}python main.py --mode daily{RESET}

  Pour lancer la newsletter hebdomadaire :
    {DIM}python main.py --mode weekly{RESET}
""")


if __name__ == "__main__":
    main()
