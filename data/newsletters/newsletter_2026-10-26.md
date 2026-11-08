# Veille Tech : Industrialiser l'Agentic AI et rationaliser nos actifs numériques

Cette semaine, la veille technologique confirme une bascule majeure : nous passons de l'expérimentation "chat" à l'ingénierie "agentique". Pour un grand groupe bancaire, cela signifie que notre priorité n'est plus seulement de générer du code ou du contenu, mais de sécuriser l'exécution, de maîtriser la consommation de jetons (FinOps IA) et d'intégrer ces agents dans une architecture de données robuste. Voici l'essentiel à retenir pour orienter notre stratégie.

---

## 🏗️ Rationalisation & simplification du SI
La leçon de Netflix et Cloudflare est claire : la dette technique n'est plus une option. L'article *[The Orchestrator's Tax](https://martinfowler.com/articles/orchestrator-tax.html)* de Martin Fowler nous rappelle que la valeur réside dans la délégation aux sous-agents pour protéger la fenêtre de contexte. Parallèlement, Netflix nous montre via ses [optimisations mémoire (100 To économisés)](https://blog.cloudflare.com/cache-transcoding/) que l'efficience algorithmique et le passage au langage Rust sont des leviers FinOps immédiats.
*   **Enjeu pour nous** : Ne cherchons pas à tout faire avec des LLM monolithiques. Appliquons le principe de Paracelse ("c'est la dose qui fait le poison") : chaque tâche doit utiliser le composant le plus frugal et déterministe possible (voir *[Sensible Default](https://martinfowler.com/bliki/SensibleDefault.html)*).

## ⚙️ Architecture évolutive & ingénierie logicielle
L'intégration de l'IA dans le cycle de vie du logiciel (SDLC) transforme nos méthodes. Le [SDK GitHub Copilot pour Java](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/) et l'usage de serveurs MCP ([Model Context Protocol](https://refactoring.fm/p/how-to-design-a-good-mcp-server)) deviennent des standards pour exposer nos capacités internes aux agents.
*   **Enjeu pour nous** : L'architecture "AI Gateway" devient le pivot de notre gouvernance. Elle permet de centraliser les garde-fous (Guardrails), l'identité des agents et l'auditabilité sémantique, comme le détaille cet article sur l'[Evolutionary Architecture](https://www.infoq.com/articles/evolutionary-architecture-pattern/).

## 🧠 Data & Agentic AI
Le passage à des systèmes multi-agents (A2A) nécessite une maîtrise du "LLM-as-a-Judge". Netflix, avec son cycle de vie pour les [évaluateurs IA](https://netflixtechblog.medium.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508), nous donne la marche à suivre : jamais d'IA en production sans une validation humaine (HITL) ancrée dans un pipeline de monitoring continu.

---

## 📊 L'Infographie Technique de la Semaine

![Analyse de la validité des modèles par des tests déterministes sur Google Cloud Platform](https://cdn-images-1.medium.com/max/1024/1*IdnKHO6yHV-y0VRXNn88YQ.png)
*(Source : [Google Cloud Community & Architecture](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e?source=rss----e52cf94d98af---4))*

**Analyse :** Ce tableau démontre pourquoi, en environnement bancaire, la croyance aveugle en un nouveau modèle est dangereuse. Avant le "fix" structurel (vérification des schémas Pydantic), les modèles échouaient à 100% sur des tâches complexes.
**Enseignement :** Pour nos projets IA sur GCP/Vertex AI, le succès ne vient pas de la taille du modèle, mais de la **rigueur du cadre d'évaluation**. L'observabilité ne doit pas se limiter au monitoring réseau, mais inclure des tests sémantiques. Si le schéma de sortie n'est pas garanti, le système n'est pas prêt pour la production.

---

## 🗺️ La Carte Stratégique (Wardley Map) de la Semaine

![Wardley Map - Visualisation de la chaîne de valeur et de l'évolution des composants](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdDK7_kvC0fkbYJNouIDIUHo0yfvBugq5bKMmUxavEs3YKYzMNHZok1ibhTtU4jGlaRGeElExA0dVfmajAKTQHNdZJFaQbzx3RgYnMX3z2I0q9KX5ITL5ViB6f6LoXYv2aCslodOxxKJXmZdq0EeL6TBFMWUO-frYqS-M3UDfMe5JgLiodljA1Rg/w400-h145/map04.png)
*(Source : [Simon Wardley - Gardeviance](https://blog.gardeviance.org/2024/02/a-good-enough-map.html))*

**Analyse stratégique :** Cette carte illustre l'évolution nécessaire des composants.
*   **Mouvement :** Les capacités de raisonnement IA basculent rapidement de la "Genèse" (propriétaire) vers le "Produit" (API managées AWS/GCP).
*   **Opportunité :** En automatisant l'inférence via des gateways, nous commoditisons cette couche pour nous concentrer sur la "Valeur Utilisateur" (en haut de la chaîne). L'inertie organisationnelle réside dans le maintien de systèmes monolithiques alors que la valeur se déplace vers des agents autonomes plus agiles.

---

## 🚀 Projets Pilotes à Lancer sous 3 Mois

1.  **Observabilité "GenAI-first"** : Déployer un outil de tracking de jetons et de coûts (type IBM Instana ou wrapper OpenTelemetry) sur une application LLM existante.
    *   *Durée* : M1 (Instrumentation) / M2 (Benchmarking coûts) / M3 (Optimisation).
2.  **AI Gateway de Groupe** : Centraliser les accès LLM via une plateforme type GCP Vertex AI avec Guardrails intégrés.
    *   *Durée* : M1 (Audit des accès actuels) / M2 (Migration des endpoints) / M3 (Reporting financier).
3.  **Human-in-the-Loop pour le Code** : Automatiser la revue de code par agent IA, avec un workflow de validation humaine stricte pour les branches critiques.
    *   *Durée* : M1 (Choix du modèle) / M2 (Configuration des règles) / M3 (Test sur 3 équipes).
4.  **Data Graph pour le KYC** : Utiliser un graphe de connaissances (Amazon Neptune/Neo4j) pour détecter les UBO (Bénéficiaires effectifs) dans les documents KYC.
    *   *Durée* : M1 (Modélisation ontologie) / M2 (POC extraction LLM) / M3 (Validation conformité).

---

**Question pour le réseau :** Si demain vos agents IA deviennent autonomes pour valider une ligne de crédit, quel est le *seul* critère non négociable que vous imposeriez dans votre pipeline d'évaluation ?