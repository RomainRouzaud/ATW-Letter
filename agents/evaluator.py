import os
import json
import time
from datetime import datetime
from agents.llm_client import LLMClient


def evaluate_article(article: dict, client: LLMClient) -> dict | None:
    """
    Uses the configured LLM to evaluate if an article is relevant for an
    Enterprise Architect in Banking/Finance/Energy/Military.
    """
    prompt = f"""
Tu es un Architecte d'Entreprise Senior dans un grand groupe bancaire européen.
Évalue l'article suivant pour voir s'il est pertinent pour ta veille technologique et fonctionnelle.
Tes domaines d'intérêt s'articulent autour de 5 axes majeurs :
1. Rationalisation & simplification du SI
2. Architecture évolutive & ingénierie logicielle
3. Data & Agentic AI
4. Agent Développeur & Développeur Augmenté (outils d'assistance au codage, IDEs agentiques comme Cursor/Windsurf/Copilot, agents logiciels autonomes SWE/Claude Code, revues de code et tests automatisés par IA, impact sur la productivité des développeurs, gestion de la dette technique et gouvernance du code généré)
5. Usage de l'IA pour le Métier Bancaire : Retail Banking (scoring crédit temps réel, assistants KYC/service client, détection de fraude transactionnelle, hyper-personnalisation), Asset Management (analyse financière et de sentiment, recherche augmentée/RAG sur rapports annuels, allocation assistée, conformité ESG), et CIB (Corporate & Investment Banking : structuration de deals, analyse de contrats et term sheets complexes, pricing & risk modeling, surveillance des marchés et post-trade)
(Tu interviens particulièrement dans les secteurs Banque, Assurance, Énergie et Militaire, avec un focus sur la scalabilité, le Cloud, la cybersécurité, les infographies d'architecture technique, les outils d'ingénierie logicielle augmentée et les Cartes de Wardley / Wardley Maps stratégiques).

Titre : {article['title']}
Source : {article['source']}
Catégorie : {article.get('category', 'Général')}
Diagrammes / Infographies présents : {len(article.get('images', []))}
Wardley Map détecté : {'Oui' if article.get('has_wardley') else 'Non'}
Thématique Agent Développeur / Dev Augmenté : {'Oui' if article.get('is_dev_agent') else 'Non'}
Contenu : {article['content'][:3000]}

Réponds au format JSON strict avec les clés suivantes :
- "relevance_score" (entier de 0 à 10 - attribue au moins 8 si l'article contient un Wardley Map pertinent, une infographie d'architecture majeure, une avancée concrète sur l'agent développeur ou un cas d'usage fort de l'IA dans les métiers bancaires Retail, Asset Management ou CIB)
- "reason" (chaîne expliquant pourquoi)
- "summary" (résumé en français de 3-4 phrases si le score est >= 7, sinon chaîne vide)
- "key_concepts" (liste de mots-clés)
"""
    for attempt in range(3):
        try:
            text = client.generate(prompt, json_mode=True)
            if text:
                # Strip markdown code fences if present
                cleaned = text.strip()
                if cleaned.startswith("```"):
                    cleaned = "\n".join(cleaned.split("\n")[1:])
                if cleaned.endswith("```"):
                    cleaned = "\n".join(cleaned.split("\n")[:-1])
                return json.loads(cleaned)
        except (json.JSONDecodeError, Exception) as e:
            if "RESOURCE_EXHAUSTED" in str(e) or "429" in str(e):
                print(f"Rate limit hit. Waiting 15 seconds before retry ({attempt+1}/3)...")
                time.sleep(15)
            else:
                print(f"Evaluation error for '{article['title']}': {e}")
                return None
    return None


def process_daily_articles(raw_filepath: str, output_dir: str = "data/summaries") -> str | None:
    if not os.path.exists(raw_filepath):
        print(f"File {raw_filepath} not found.")
        return None

    with open(raw_filepath, "r", encoding="utf-8") as f:
        articles = json.load(f)

    client = LLMClient()
    print(f"[Evaluator] Provider LLM actif : {client.provider} / {client.model}")

    os.makedirs(output_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    summary_filepath = os.path.join(output_dir, f"summaries_{today}.json")

    evaluated_articles = []

    for article in articles:
        print(f"Evaluating: {article['title']}...")
        evaluation = evaluate_article(article, client)
        if evaluation and evaluation.get("relevance_score", 0) >= 7:
            print(f" -> Keep! (Score >= 7)")
            article["evaluation"] = evaluation
            evaluated_articles.append(article)
        else:
            print(f" -> Skip. (Score < 7 or error)")
        time.sleep(3)

    with open(summary_filepath, "w", encoding="utf-8") as f:
        json.dump(evaluated_articles, f, ensure_ascii=False, indent=2)

    return summary_filepath


if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    process_daily_articles(f"data/raw/articles_{today}.json")
