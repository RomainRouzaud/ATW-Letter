import os
import json
import glob
from datetime import datetime
from agents.llm_client import LLMClient


def load_weekly_summaries(summary_dir: str = "data/summaries") -> list:
    summaries = []
    filepaths = glob.glob(os.path.join(summary_dir, "*.json"))
    for filepath in filepaths:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            summaries.extend(data)
    return summaries


def is_gcp_or_ibm(item: dict) -> bool:
    """Helper to detect if an asset is related to Google Cloud or IBM Cloud."""
    text = (
        str(item.get("title", "")) + " " +
        str(item.get("source", "")) + " " +
        str(item.get("alt", "")) + " " +
        str(item.get("link", ""))
    ).lower()
    return any(k in text for k in [
        "gcp", "google cloud", "vertex", "bigquery", "gke",
        "ibm", "watsonx", "instana", "openshift"
    ])


def is_valid_image_url(url: str) -> bool:
    """Filter out tracking pixels and beacons."""
    if not url:
        return False
    u = url.lower()
    return not any(bad in u for bad in [
        "medium.com/_/stat", "stat?", "clientviewed", "pixel",
        "tracking", "1x1", "feedburner", "beacon", "badge"
    ])


def find_visual_assets(summaries: list) -> tuple[list, list]:
    """
    Find authentic infographics and Wardley Maps extracted from the sources.
    Prioritizes IBM Cloud and Google Cloud Platform (GCP) infographics.
    Returns: (infographics_candidates, wardley_candidates)
    """
    all_infographics = []
    wardley_maps = []
    seen_urls = set()

    # 1. Search directly in evaluated summaries
    for s in summaries:
        images = s.get("images", [])
        if not images:
            continue
        is_wardley = (
            s.get("has_wardley", False)
            or "wardley" in s.get("source", "").lower()
            or "wardley" in s.get("title", "").lower()
            or any("wardley" in str(tag).lower() for tag in s.get("tags", []))
        )
        for img in images:
            url = img.get("url") if isinstance(img, dict) else img
            alt = img.get("alt", s.get("title", "")) if isinstance(img, dict) else s.get("title", "")
            if not is_valid_image_url(url) or url in seen_urls:
                continue
            seen_urls.add(url)
            asset = {
                "title": s.get("title", "Sans titre"),
                "source": s.get("source", "Source"),
                "link": s.get("link", ""),
                "img_url": url,
                "alt": alt
            }
            if is_wardley:
                wardley_maps.append(asset)
            else:
                all_infographics.append(asset)

    # 2. Search recent raw articles in data/raw/*.json to retrieve fresh IBM / GCP infographics & Wardley maps
    for fpath in sorted(glob.glob("data/raw/*.json"), reverse=True):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                raw_articles = json.load(f)
                for a in raw_articles:
                    is_w = (
                        a.get("has_wardley", False)
                        or "wardley" in a.get("source", "").lower()
                        or "wardley" in a.get("title", "").lower()
                    )
                    if a.get("images"):
                        for img in a["images"]:
                            url = img.get("url") if isinstance(img, dict) else img
                            alt = img.get("alt", a.get("title", "")) if isinstance(img, dict) else a.get("title", "")
                            if not is_valid_image_url(url) or url in seen_urls:
                                continue
                            seen_urls.add(url)
                            item = {
                                "title": a.get("title", "Document"),
                                "source": a.get("source", "Source"),
                                "link": a.get("link", ""),
                                "img_url": url,
                                "alt": alt
                            }
                            if is_w:
                                wardley_maps.append(item)
                            else:
                                all_infographics.append(item)
        except Exception:
            pass

    # Separate into GCP / IBM prioritized infographics vs others
    gcp_ibm_candidates = [i for i in all_infographics if is_gcp_or_ibm(i)]
    other_candidates = [i for i in all_infographics if not is_gcp_or_ibm(i)]

    # Ranked infographics: GCP and IBM Cloud at the top
    prioritized_infographics = gcp_ibm_candidates + other_candidates

    return prioritized_infographics, wardley_maps


def draft_weekly_newsletter(summaries: list) -> str | None:
    if not summaries:
        print("No summaries found for this week.")
        return None

    client = LLMClient()
    print(f"[Writer] Provider LLM actif : {client.provider} / {client.model}")

    prompt_data = ""
    for s in summaries:
        eval_data = s.get("evaluation", {})
        prompt_data += (
            f"- Titre: {s['title']}\n"
            f"  Source: {s['source']}\n"
            f"  Lien: {s['link']}\n"
            f"  Résumé: {eval_data.get('summary', '')}\n"
            f"  Concepts clés: {', '.join(eval_data.get('key_concepts', []))}\n\n"
        )

    # Find genuine visual assets
    infographics, wardley_maps = find_visual_assets(summaries)

    infographics_section = "Aucune infographie trouvée."
    if infographics:
        infographics_section = "Voici les infographies d'architecture RÉELLES extraites de nos sources.\n(IMPORTANT : Priorité absolue donnée aux infographies IBM Cloud et Google Cloud Platform / GCP) :\n"
        for idx, item in enumerate(infographics[:8], 1):
            is_priority = is_gcp_or_ibm(item)
            priority_tag = " ⭐ [PRIORITAIRE - IBM Cloud / Google Cloud]" if is_priority else ""
            infographics_section += (
                f"{idx}. Article : {item['title']}{priority_tag}\n"
                f"   Source : {item['source']} ({item['link']})\n"
                f"   Image URL : {item['img_url']}\n"
                f"   Description / Alt : {item['alt']}\n\n"
            )

    wardley_section = "Aucun Wardley Map trouvé."
    if wardley_maps:
        wardley_section = "Voici les Cartes de Wardley (Wardley Maps) RÉELLES extraites de nos sources (choisis obligatoirement l'une de ces URLs exactes) :\n"
        for idx, item in enumerate(wardley_maps[:4], 1):
            wardley_section += (
                f"{idx}. Titre : {item['title']}\n"
                f"   Source : {item['source']} ({item['link']})\n"
                f"   Image URL : {item['img_url']}\n"
                f"   Description / Alt : {item['alt']}\n\n"
            )

    prompt = f"""
Tu es un Architecte d'Entreprise Senior dans un grand groupe bancaire européen (BNP Paribas).
Tu rédiges ta newsletter hebdomadaire de veille technologique (pour LinkedIn et ton réseau interne IT).
Voici les articles pertinents que tu as sélectionnés cette semaine :

{prompt_data}

---
DOCUMENTS VISUELS RÉELS ISSUS DE NOS SOURCES :

{infographics_section}

{wardley_section}
---

Rédige un article professionnel, engageant et structuré en français.
Consignes :
1. Titre accrocheur et professionnel.
2. Introduction courte qui met en contexte la semaine (ex: focus sur l'IA, le Cloud hybride, la gouvernance ou la rationalisation).
3. Regroupe impérativement les articles de fond autour de nos 5 axes stratégiques clairs (utilise des titres de niveau 2 avec émojis) :
   - "## 1. 🔄 Rationalisation & Simplification du SI"
   - "## 2. 🏗️ Architecture Évolutive & Ingénierie Logicielle"
   - "## 3. 🧠 Data & Agentic AI"
   - "## 4. 💻 Agent Développeur & Développeur Augmenté" (Consacre obligatoirement une section complète et approfondie aux agents développeurs et au développeur augmenté : outils de génération/complétion de code, IDEs agentiques comme Cursor/Windsurf/Copilot/Continue, agents logiciels autonomes type SWE/Claude Code, revues de code et tests automatisés par IA, impact sur la productivité et l'expérience développeur DevEx, gestion de la dette technique générée par IA et gouvernance de la sécurité/conformité du code).
   - "## 5. 🏦 IA & Métiers Bancaires : Retail, Asset Management, CIB & Digital Assets" (Consacre obligatoirement une section d'analyse de fond dédiée aux cas d'usage métiers bancaires de l'IA, structurée rigoureusement avec les 4 sous-parties suivantes :
     * "### Retail Banking (Banque de détail)" : scoring crédit temps réel et octroi augmenté, agents conversationnels bancaires et support client autonome, KYC/onboarding digital sans friction, détection de fraude transactionnelle temps réel, hyper-personnalisation et automatisation back-office.
     * "### Asset Management (Gestion d'actifs)" : analyse de sentiment de marché, synthèse automatique de rapports financiers et earnings calls, recherche augmentée (RAG) sur données non structurées, copilote d'allocation de portefeuille et génération de thèses d'investissement, conformité ESG et reporting automatisé.
     * "### Corporate & Investment Banking (CIB / Banque de Financement et d'Investissement)" : structuration de deals et M&A assistés par IA, extraction et audit automatisés de contrats complexes / term sheets / prospectus, modélisation des risques et pricing de dérivés en temps réel, surveillance des marchés et détection d'abus de marché / délit d'initié, réconciliation et automatisation post-trade.
      * "### Digital Assets & Crypto" : tokenisation d'actifs réels (Real-World Assets / RWA) et smart contracts sur blockchains permissionnées (Hyperledger, Ethereum Enterprise), IA pour la surveillance de marchés crypto et détection d'anomalies on-chain, automatisation du reporting réglementaire crypto (MiCA, Travel Rule), gestion des risques de liquidité DeFi, valorisation et audit de portefeuilles d'actifs numériques, infrastructure de custody institutionnelle augmentée par IA.
     Pour chaque pôle métier, détaille les patterns d'architecture technique (GraphRAG, modèles spécialisés SLM/LLM, garde-fous déterministes, intégration legacy core-banking), les gains chiffrés et la conformité réglementaire bancaire : DORA, EU AI Act, RGPD, MiCA, auditabilité et explicabilité).
4. Synthétise les retours d'expérience sans faire un simple "catalogue" de liens. Mets en valeur *pourquoi* c'est important pour les grandes entreprises.
5. Inclus systématiquement les liens vers les articles originaux.

6. **SECTION OBLIGATOIRE : "## 📊 L'Infographie Technique de la Semaine"**
   - **CIBLAGE STRICT : Tu DOIS sélectionner en priorité une infographie en lien avec IBM Cloud (ou watsonx / IBM Instana / OpenShift) ou avec Google Cloud Platform (GCP / Vertex AI / GKE)** parmi les options prioritaires réelles listées ci-dessus.
   - Affiche l'image au format Markdown strict : `![Description précise de l'architecture](URL_EXACTE_DE_L_IMAGE)`.
   - Analyse ce schéma d'architecture sous l'angle grand groupe bancaire :
     * Architecture des composants et flux de données.
     * Enjeux de performance, observabilité GenAI, FinOps ou passage à l'échelle sur IBM Cloud / GCP.
     * Enseignements opérationnels pour nos projets de transformation d'entreprise.
   - Mentionne la source d'origine avec son lien direct.
   - ⚠️ RÈGLE STRICTE : N'INVENTE AUCUNE URL d'image. Utilise exclusivement l'une des URLs réelles marquées ci-dessus.

7. **SECTION OBLIGATOIRE : "## 🗺️ La Carte Stratégique (Wardley Map) de la Semaine"**
   - Sélectionne UN Wardley Map parmi la liste des cartes réelles fournies ci-dessus (issues de Simon Wardley ou de Wardley Maps publication).
   - Affiche l'image de la carte au format Markdown strict : `![Wardley Map - Titre](URL_EXACTE_DE_L_IMAGE)`.
   - Fournis une analyse stratégique basée sur la méthodologie de Simon Wardley :
     * Chaîne de valeur (axe vertical : du besoin utilisateur aux composants d'infrastructure).
     * Évolution des composants (axe horizontal : Genèse -> Sur mesure -> Produit -> Commodité).
     * Mouvements stratégiques, inerties organisationnelles et opportunités d'industrialisation sur le cloud (GCP / IBM Cloud).
     * Fais le lien avec nos thématiques (commoditisation de l'inférence, plateformes managées, gestion des dépendances).
   - Mentionne la source d'origine avec son lien direct.
   - ⚠️ RÈGLE STRICTE : N'INVENTE AUCUNE URL d'image. Utilise exclusivement l'une des URLs réelles listées ci-dessus.

8. Une section dédiée intitulée "## 🚀 Projets Pilotes à Lancer sous 3 Mois" :
   Pour chaque grand thème identifié dans la veille (dont obligatoirement 1 projet pilote dédié à l'Agent Développeur / Développeur Augmenté dans un environnement d'entreprise sécurisé), propose 1 projet pilote concret avec :
   - **Objectif** : L'hypothèse à valider (issue directement des articles de la semaine).
   - **Périmètre équipe** : Composé pour une équipe de ~10 personnes (profils recommandés : ex. 2 devs backend, 1 archi, 1 PO, 1 data engineer…).
   - **Durée** : 3 mois, découpée en 3 jalons mensuels (M1 / M2 / M3).
   - **Critères de succès** : 2-3 métriques mesurables pour valider (ou invalider) l'hypothèse.
   - **Risques** : 1-2 risques à surveiller et comment les mitiger.
   Propose entre 3 et 4 projets pilotes au total. Rends-les concrets, réalistes et directement actionnables dans un contexte grand groupe.

9. **SECTION OBLIGATOIRE : "## 🏢 Projets Réels Passés à l'Échelle"** (à insérer impérativement après les Projets Pilotes) :
   Présente 4 à 5 retours d'expérience concrets d'entreprises ou institutions financières ayant déployé en production à grande échelle (ou ayant fait l'objet d'une démonstration publique/conférence/publication technique de référence), couvrant nos thématiques stratégiques dont les métiers bancaires :
   - **Cas 1 — Rationalisation & Simplification du SI** (ex: migration cloud massive, extinction de datacenters legacy, consolidation d'architectures monolithiques chez Netflix, Capital One, Uber, Airbnb ou une grande banque).
   - **Cas 2 — Architecture Évolutive & Ingénierie Logicielle** (ex: bascule event-driven, architectures Zero-Trust, API Gateway globale, microservices résilients chez Stripe, Cloudflare, Shopify, DoorDash ou Spotify).
   - **Cas 3 — Data & Agentic AI** (ex: multi-agents en production bancaire, Lakehouse Apache Iceberg à l'échelle pétaoctet, GraphRAG pour la détection de fraude ou conformité chez Morgan Stanley, Klarna, Intuit, Bloomberg ou Neo4j).
   - **Cas 4 — Agent Développeur & Développeur Augmenté** (ex: déploiement à large échelle d'assistants de code ou d'IDEs agentiques, agents de tests/revues de code comme GitHub Copilot, Meta SapFix/Sapienz, Amazon Q Developer, Google Cider/AI Code Review chez un grand groupe bancaire, Meta, Amazon ou Google, avec métriques de productivité et gouvernance).
   - **Cas 5 — IA Métiers Bancaires (Retail, Asset Management ou CIB)** (ex: JPMorgan COiN / LLM Suite pour l'analyse de contrats CIB et recherche financière, Morgan Stanley Wealth Management Copilot, Klarna AI Assistant pour le retail banking, ou MUFG Bank AI Flowchart).

   Pour chacun des cas, applique cette structure claire et homogène :
   - `### [Nom de l'Entreprise] : [Titre du projet / transformation]`
   - **Catégorie** : [Nom de la catégorie]
   - **Contexte & Verrou Initial** : La problématique de départ à grande échelle.
   - **Architecture & Déploiement** : Les composants techniques, patterns choisis et l'échelle (utilisateurs, transactions, volume de code, nœuds de calcul).
   - **Impact Chiffré & Résultats** : Métriques concrètes vérifiables (coûts %, vélocité %, MTTR, qualité).
   - **Référence Publique** : Lien ou mention de la conférence technique (ex. AWS re:Invent, QCon, InfoQ, KubeCon) ou du TechBlog d'ingénierie officiel.

10. Conclusion rapide avec une question ouverte pour engager la discussion.

Réponds uniquement avec le texte de l'article en format Markdown.
"""

    text = client.generate(prompt, json_mode=False)
    if not text:
        print("Error generating newsletter: LLM returned empty response.")
        return None
    return text


def save_newsletter(content: str, output_dir: str = "data/newsletters") -> str:
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = os.path.join(output_dir, f"newsletter_{today}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


if __name__ == "__main__":
    summaries = load_weekly_summaries()
    article = draft_weekly_newsletter(summaries)
    if article:
        saved_path = save_newsletter(article)
        print(f"Newsletter drafted and saved to {saved_path}")
