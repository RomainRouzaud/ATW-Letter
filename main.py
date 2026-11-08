import argparse
import os
from dotenv import load_dotenv

load_dotenv()

from agents.collector import load_sources, collect_daily_articles, save_raw_articles
from agents.evaluator import process_daily_articles
from agents.writer import load_weekly_summaries, draft_weekly_newsletter, save_newsletter
from agents.mailer import send_newsletter


def run_daily():
    print("=== Démarrage du Job Quotidien ===")
    sources = load_sources()
    print(f"{len(sources)} sources chargées.")

    articles = collect_daily_articles(sources)
    if not articles:
        print("Aucun nouvel article trouvé.")
        return

    raw_filepath = save_raw_articles(articles)
    print(f"{len(articles)} articles bruts sauvegardés dans {raw_filepath}.")

    print("--- Évaluation LLM ---")
    summary_filepath = process_daily_articles(raw_filepath)
    if summary_filepath:
        print(f"Résumés sauvegardés dans {summary_filepath}.")
    print("=== Fin du Job Quotidien ===")


def run_weekly(send_email: bool = False, generate_html: bool = True):
    print("=== Démarrage du Job Hebdomadaire ===")
    summaries = load_weekly_summaries()
    print(f"{len(summaries)} articles pertinents trouvés pour cette semaine.")

    article_content = draft_weekly_newsletter(summaries)
    if not article_content:
        print("Échec de la rédaction de la newsletter.")
        print("=== Fin du Job Hebdomadaire ===")
        return

    saved_path = save_newsletter(article_content)
    print(f"Newsletter hebdomadaire sauvegardée dans {saved_path}.")

    if generate_html:
        print("--- Génération de la Page HTML Multilingue (7 langues) ---")
        try:
            from scripts.build_multilingual_page import generate_multilingual_publication
            html_paths = generate_multilingual_publication(base_filepath=saved_path)
            if html_paths:
                print(f"✓ Page HTML multilingue prête : {html_paths.get('project_html')}")
        except Exception as e:
            print(f"⚠️ Erreur lors de la génération de la page HTML multilingue : {e}")

    if send_email:
        print("--- Envoi Email ---")
        success = send_newsletter(article_content)
        if not success:
            print("⚠️  L'envoi email a échoué. La newsletter reste disponible localement.")
    else:
        print("ℹ️  Envoi email désactivé (relancez avec --send-email pour envoyer).")

    print("=== Fin du Job Hebdomadaire ===")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Système de Veille Technologique Agentique")
    parser.add_argument(
        "--mode",
        choices=["daily", "weekly"],
        required=True,
        help="Mode d'exécution: daily ou weekly"
    )
    parser.add_argument(
        "--send-email",
        action="store_true",
        default=False,
        help="Envoie la newsletter par email après génération (mode weekly uniquement)"
    )
    parser.add_argument(
        "--no-html",
        action="store_true",
        default=False,
        help="Désactive la génération de la page HTML multilingue (mode weekly)"
    )
    args = parser.parse_args()

    if args.mode == "daily":
        run_daily()
    elif args.mode == "weekly":
        run_weekly(send_email=args.send_email, generate_html=not args.no_html)
