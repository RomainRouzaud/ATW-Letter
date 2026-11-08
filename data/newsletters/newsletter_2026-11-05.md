# Veille Technologique #124 : L'ère de l'Architecture Agentique et de l'Ingénierie Augmentée

Cette semaine, la veille technologique confirme une bascule majeure dans nos pratiques : nous passons de l'expérimentation "chat-based" à une **ingénierie agentique industrielle**. Le focus n'est plus seulement sur la génération de code, mais sur la gouvernance, le coût unitaire (FinOps) et la maîtrise des chaînes de dépendances dans des systèmes complexes.

---

## 1. 🔄 Rationalisation & Simplification du SI
La leçon principale des retours d'expérience de Netflix et Cloudflare est claire : la performance est une fonction de la simplicité. Cloudflare a économisé 100 To de RAM via des optimisations algorithmiques (consistent hashing en Rust), tandis que Netflix réévalue ses systèmes d'autoscaling Flink pour standardiser sur l'open-source communautaire. Pour un grand groupe bancaire, cela souligne l'importance d'éviter la prolifération de composants propriétaires ("build vs adopt") et de se concentrer sur des fondations robustes et standardisées.

*   [Optimisation mémoire chez Cloudflare](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)
*   [Autoscaling Apache Flink chez Netflix](https://netflixtechblog.com/a-tale-of-two-flink-autoscalers-e9f6a1b1492b)

## 2. 🏗️ Architecture Évolutive & Ingénierie Logicielle
L'émergence des **AI Gateways** et du **Model Context Protocol (MCP)** est le sujet de fond pour notre architecture. Ces patterns permettent de découpler les modèles IA de nos applications, offrant un point de contrôle unique pour l'audit, la conformité et la sécurité. Le passage à des architectures *stateless* pour le protocole MCP est une opportunité clé pour nos déploiements serverless (AWS Lambda, Bedrock), permettant une scalabilité horizontale sans gestion de sessions complexes.

*   [AI Gateway et Architecture Évolutive](https://www.infoq.com/articles/evolutionary-architecture-pattern/)
*   [MCP et Architecture Stateless](https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/)

## 3. 🧠 Data & Agentic AI
La donnée reste le carburant, mais sa structure est désormais dictée par les besoins des agents. Les retours sur le **GraphRAG** (couplage de bases de données orientées graphes comme Amazon Neptune avec LLM) montrent une réduction drastique (jusqu'à 90%) des efforts de modélisation métier. En ancrant les LLM dans des ontologies rigoureuses, nous éliminons le risque d'hallucination et garantissons la conformité réglementaire nécessaire dans nos processus KYC/AML.

*   [MUFG Bank : 90% de gain sur la modélisation](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)
*   [Récupération contextuelle et GraphRAG](https://neo4j.com/blog/agentic-ai/contextual-retrieval/)

## 4. 💻 Agent Développeur & Développeur Augmenté
Nous entrons dans l'ère de l'**ingénierie logicielle augmentée**. Les agents ne sont plus des aides à la saisie, mais des orchestrateurs (ex: Claude Code, Qodo). 

*   **Le paradoxe de la productivité** : Les outils comme GitHub Copilot (via son SDK pour Java) ou Cursor transforment la nature du travail. Le goulot d'étranglement est passé du codage à la revue de code.
*   **Gouvernance et Sécurité** : L'automatisation des revues et des tests par des agents (ex: Google Mantis) est désormais impérative. Toutefois, nous devons rester vigilants face au *Skill Decay* (érosion des compétences techniques) : l'humain doit rester le "pilote" qui valide la structure architecturale.
*   **Infrastructure** : GitHub et Anthropic redéfinissent le contrôle de version pour supporter des agents qui "codent en continu" sans verrouiller les dépôts.

*   [GitHub Copilot SDK for Java](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)
*   [Gouvernance des agents développeurs avec JetBrains](https://blog.jetbrains.com/ai/2026/11/livestream-scaling-agentic-development-with-air-governance/)

---

## 📊 L'Infographie Technique de la Semaine

![Analyse de la validation des modèles d'IA par tests déterministes (Google Cloud/Vertex AI)](https://cdn-images-1.medium.com/max/1024/1*L-sfIHDoKW1COd8Dyq7Pkg.png)

*Source : [Google Cloud Community - A New Model Is Not an Upgrade Until Your Evals Say So](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e)*

**Analyse** : Ce schéma illustre l'importance capitale des tests déterministes (basés sur des schémas Pydantic et des tests de conformité) lors de l'intégration de nouveaux LLM. Avant la correction du schéma, le taux de correspondance aux attentes métier était médiocre. Après, la performance bondit. 
**Enseignement opérationnel** : Ne jamais déployer un agent en production sans une batterie de tests structurels (canaries, contrôle de schéma). Dans une banque, un agent qui hallucine un format de fichier de transaction est un risque critique.

---

## 🗺️ La Carte Stratégique (Wardley Map) de la Semaine

![Wardley Map - L'Évolution du Stack Applicatif & du Serverless](https://cdn-images-1.medium.com/max/1024/1*-oZD4wPJkqOPQbuLPSCF0Q.jpeg)

*Source : [Simon Wardley — On playing chess (Wardley Maps Publication)](https://medium.com/wardleymaps/on-playing-chess-2634b825dbac)*

**Analyse** : Cette carte met en lumière l'inversion de la gravité de l'ingénierie logicielle : en poussant le calcul et le runtime d'exécution vers l'utilité publique (*Commodity/Utility* via le Serverless et les plateformes managées), l'infrastructure s'efface totalement pour les développeurs. Le temps historiquement gaspillé dans le *Yak Shaving* (configuration de serveurs, patchs d'OS, plannings de capacité) disparaît au profit de la logique métier directe.
**Mouvement stratégique** : Avec l'irruption des agents développeurs, la production de code elle-même entame son glissement vers la commodité industrielle. La valeur ajoutée de l'ingénieur ne réside plus dans la frappe de lignes de code, mais remonte au sommet de la chaîne de valeur : l'orchestration des flux d'agents, la sécurité contextuelle et la résilience globale du SI.

---

## 🚀 Projets Pilotes à Lancer sous 3 Mois

1.  **Pilot Agent Développeur (Gouverné)** :
    *   **Objectif** : Valider l'usage d'un IDE agentique (type Cursor/Continue) sur un dépôt Legacy avec *Air Governance* pour monitorer les coûts.
    *   **Périmètre** : 1 équipe de 10 personnes.
    *   **Jalons** : M1 (Installation/Policy), M2 (Tâches de maintenance simples), M3 (Mesure productivité).
    *   **Critères succès** : Réduction du temps de debug de 20%, respect du budget tokens.

2.  **Pilot GraphRAG pour la Conformité** :
    *   **Objectif** : Automatiser l'extraction d'UBO (Bénéficiaire Effectif) à partir de documents KYC via Amazon Neptune.
    *   **Périmètre** : Data Engineer, Data Scientist, Expert Conformité.
    *   **Critères succès** : Précision > 95% par rapport à l'analyse manuelle.

3.  **Pilot AI Gateway** :
    *   **Objectif** : Centraliser tous les appels LLM via une Gateway pour monitorer les coûts et le contenu.
    *   **Périmètre** : Archi, Ops.
    *   **Critères succès** : Visibilité 100% des requêtes, coût/token maîtrisé.

---

## 🏢 Projets Réels Passés à l'Échelle

1.  **MUFG Bank (Rationalisation)** : 
    *   **Projet** : Ontology-grounded AI pour la standardisation des flux opérationnels globaux (Amazon Neptune/Bedrock). 
    *   **Résultat** : Réduction de 90% du temps de documentation des procédures (11 jours -> 1 jour). [Référence : AWS Database Blog](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

2.  **Netflix (Architecture Évolutive)** : 
    *   **Projet** : Stratum Resource Tuner (Automated Right-Sizing).
    *   **Résultat** : Optimisation automatisée des ressources conteneurs, réduisant drastiquement les coûts de run. [Référence : Netflix Tech Blog](https://netflixtechblog.medium.com/netflix-stratum-media-processing-automated-container-right-sizing-ddf9aa68a801)

3.  **Capital One (Data & Agentic AI)** : 
    *   **Projet** : Déploiement de systèmes d'agents pour le raisonnement fidèle sur le code.
    *   **Résultat** : Industrialisation de la sécurité dans le cycle de vie logiciel via des outils comme FinRT. [Référence : Capital One Tech](https://medium.com/capital-one-tech/advancing-safe-agentic-ai-asks-symposium-highlights-bbba40b19784)

4.  **Dynata (Développeur Augmenté)** : 
    *   **Projet** : Méthodologie AI-DLC couplée à Kiro IDE.
    *   **Résultat** : Livraison de fonctionnalités complexes en 1 sprint au lieu de 4, via une intégration étroite entre documentation (Jira/Confluence) et code. [Référence : AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/)

---

*La question pour nous cette semaine : Sommes-nous prêts à accepter que notre valeur ajoutée de demain ne soit plus dans la ligne de code, mais dans la capacité à orchestrer les agents qui l'écrivent et la valident ?*