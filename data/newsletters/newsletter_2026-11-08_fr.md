# **🚀 IA Agentique, Cloud Hybride & Rationalisation : La Veille Stratégique qui Redéfinit nos Architectures**

**Cette semaine, la veille technologique met en lumière des avancées majeures en matière d’IA agentique, de rationalisation du SI et d’architectures évolutives.** Entre la gestion des coûts des agents autonomes, la standardisation des processus métiers par l’ontologie, et l’émergence des IDEs agentiques, les enjeux de productivité, de gouvernance et de résilience n’ont jamais été aussi critiques pour les grandes entreprises.

Les retours d’expérience de Netflix, GitHub, AWS et Capital One illustrent une tendance claire : **l’IA n’est plus un simple outil d’automatisation, mais un acteur central de nos systèmes**, exigeant une refonte des processus, des architectures et des compétences.

---
---

## **1. 🔄 Rationalisation & Simplification du SI**

### **L’IA comme levier de standardisation des processus**
Les grandes organisations bancaires et industrielles sont souvent confrontées à une **fragmentation des processus métiers** due à une croissance décentralisée. MUFG Bank a résolu ce défi en déployant une solution d’**IA basée sur des ontologies** couplée à Amazon Neptune et Bedrock. Résultat : une réduction de **90 % du temps de développement** des procédures opérationnelles (passant de 11 à 1 jour/homme), tout en garantissant une standardisation cohérente à l’échelle mondiale.
→ [Lire l’article](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

**Pourquoi c’est critique ?**
- **Dette opérationnelle** : Les processus fragmentés alourdissent la maintenance et augmentent les risques de non-conformité.
- **Gouvernance centralisée** : Une ontologie métier permet de **démocratiser l’accès aux données** tout en contrôlant leur usage via des garde-fous IA.
- **ROI immédiat** : La réduction des coûts de documentation et de formation est un argument clé pour les directions financières.

---
### **La fin des runbooks obsolètes : vers une observabilité agentique**
L’accélération du développement par l’IA rend les **runbooks manuels obsolètes** avant même leur mise à jour. Sourcegraph propose une approche radicale : utiliser des outils de **recherche sémantique profonde** et le **protocole MCP (Model Context Protocol)** pour ancrer la gestion des incidents directement dans le code source actuel.
→ [Lire l’article](https://sourcegraph.com/blog/sre-runbooks-ai-driven-development)

**Pourquoi c’est critique ?**
- **Réduction du MTTR** : Les équipes SRE passent moins de temps à chercher des solutions manuelles.
- **Traçabilité des décisions** : Chaque incident est lié à une modification de code, avec un historique complet.
- **Adaptation aux agents** : Les systèmes doivent être conçus pour des **lecteurs automatisés** (robots/IA) plutôt que pour des humains.

---
### **Cloud Sovereignty & Post-Quantum : les nouvelles frontières de la cybersécurité**
Cloudflare introduit une solution de **gestion de clés géographiquement restreintes** utilisant la **cryptographie post-quantique (PQ GeoKey Manager)**. Cette innovation répond au besoin de **souveraineté des données** en garantissant que le déchiffrement ne s’opère que sur des serveurs situés dans des zones géographiques autorisées.
→ [Lire l’article](https://blog.cloudflare.com/post-quantum-geo-key-manager/)

**Pourquoi c’est critique ?**
- **Conformité réglementaire** : Essentiel pour les banques européennes soumises au RGPD et à l’EU AI Act.
- **Résilience face aux attaques futures** : Préparation aux menaces quantiques ("harvest now, decrypt later").
- **Réduction des risques de supply chain** : Contrôle strict des tiers de confiance.

---
### **FinOps IA : mesurer le vrai coût des agents autonomes**
GitHub Engineering démontre que **réduire localement les tokens par appel d’outil** peut s’avérer contre-productif si cela force l’IA à relancer des commandes pour récupérer le contexte manquant. Leur approche holistique (compression du bruit, suppression du formatage inutile) optimise le **coût global d’une tâche** sans sacrifier la qualité.
→ [Lire l’article](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)

**Pourquoi c’est critique ?**
- **Visibilité granulaire** : Le coût par token doit inclure l’infrastructure (calcul, refroidissement, réseau).
- **Optimisation systémique** : Les gains locaux ne suffisent pas ; il faut repenser l’ensemble du pipeline.
- **Alignement avec les directions financières** : Les DAF exigent des métriques actionnables pour justifier les investissements IA.

---
---

## **2. 🏗️ Architecture Évolutive & Ingénierie Logicielle**

### **Les architectures "Agent-first" : repenser les fondations du SI**
Microsoft Azure souligne que les **applications agentiques** (capables d’agir en boucle continue sans intervention humaine) nécessitent une infrastructure dédiée. Leur vision avec **Azure Foundry et Entra Agent ID** vise à apporter aux architectures d’agents la rigueur et la conformité exigées par les grandes entreprises.
→ [Lire l’article](https://azure.microsoft.com/en-us/blog/designing-agent-first-platforms-what-changes-when-agents-do-the-work/)

**Pourquoi c’est critique ?**
- **Identité et gouvernance** : Les agents doivent avoir une identité propre, traçable et contrôlable.
- **Sécurité Zero Trust** : Les frontières de défense doivent être déplacées vers la couche d’outillage.
- **Traçabilité des décisions** : Chaque action d’un agent doit être auditée et réversible.

---
### **La dérive de la résilience : quand les diagrammes d’architecture mentent**
Azure met en lumière le phénomène de **"résilience drift"** : les changements opérationnels continus rendent obsolètes les diagrammes théoriques et réintroduisent des **points de défaillance uniques**. La résilience doit être traitée comme une **propriété dynamique**, mesurée et validée en continu.
→ [Lire l’article](https://azure.microsoft.com/en-us/blog/your-architecture-diagram-is-not-your-resilience/)

**Pourquoi c’est critique ?**
- **Validation continue** : Les architectures doivent être testées en production (ex : chaos engineering).
- **Dépendance aux modèles IA** : Les composants critiques incluent désormais des pipelines de données et des inférences LLM.
- **Continuité d’activité** : La tolérance aux pannes doit s’étendre aux services d’IA.

---
### **Multi-Region Resilience : l’art de l’orchestration hybride**
AWS Architecture Blog propose une architecture **active-active multi-régions** pour les ressources CloudFormation personnalisées, avec des **verrous distribués basés sur DynamoDB Global Tables** pour prévenir les exécutions en double et assurer un basculement automatisé.
→ [Lire l’article](https://aws.amazon.com/blogs/architecture/building-multi-Region-resiliency-for-AWS-CloudFormation-custom-resource-deployment/)

**Pourquoi c’est critique ?**
- **Disaster Recovery (DR)** : Les banques doivent garantir un **RTO/RPO minimal** pour les applications critiques.
- **Souveraineté des données** : Les données sensibles ne doivent jamais quitter leur juridiction.
- **Simplicité opérationnelle** : Les équipes doivent pouvoir tester et valider les plans de reprise sans complexité excessive.

---
### **Oracle Database sur AWS : la migration hybride maîtrisée**
AWS détaille comment déployer une **Oracle Database 19c hautement disponible** sur Amazon Elastic VMware Service (EVS) avec **Amazon FSx for NetApp ONTAP** comme stockage NFS. La solution permet de conserver l’outillage VMware existant tout en bénéficiant de **latences infra-millisecondes** et d’un **plan de reprise d’activité (PRA) inter-régions**.
→ [Lire l’article](https://aws.amazon.com/blogs/architecture/architect-highly-available-oracle-database-on-amazon-evs-and-fsx-for-ontap/)

**Pourquoi c’est critique ?**
- **Compatibilité legacy** : Les banques ne peuvent pas se permettre de tout réécrire.
- **Performance et résilience** : Les latences doivent être inférieures à la milliseconde pour les transactions financières.
- **Coûts maîtrisés** : L’optimisation du stockage et des sauvegardes réduit les coûts opérationnels.

---
---

## **3. 🧠 Data & Agentic AI**

### **GraphRAG : l’IA agentique au service de la conformité bancaire**
Neo4j démontre comment les **bases de données orientées graphes** permettent de visualiser des réseaux complexes de fraude financière. Leur outil **Linkurious Enterprise**, couplé à Amazon Neptune, accélère les investigations AML (Anti-Money Laundering) jusqu’à **10 fois** en fournissant une vue holistique des relations entre entités.
→ [Lire l’article](https://aws.amazon.com/blogs/database/intuitive-risk-investigation-with-amazon-neptune-and-linkurious-enterprise/)

**Pourquoi c’est critique ?**
- **Détection des bénéficiaires effectifs (UBO)** : Les structures imbriquées sont impossibles à analyser manuellement.
- **Conformité réglementaire** : Les régulateurs exigent une traçabilité des flux financiers.
- **Scalabilité** : Les graphes permettent de gérer des **pétabytes de données** sans perte de performance.

---
### **Text-to-SQL & Metadata Enrichment : démocratiser l’accès aux données**
IBM watsonx.data Intelligence transforme des tables de bases de données brutes en **actifs sémantiquement riches** grâce à l’enrichissement des métadonnées. Leur solution permet d’interroger des données en langage naturel via une API FastAPI, tout en garantissant la gouvernance.
→ [Lire l’article](https://medium.com/ibm-data-ai/ibm-watsonx-data-intelligence-metadata-enrichment-text-to-sql-bf03eef1451b)

**Pourquoi c’est critique ?**
- **Productivité des métiers** : Les analystes financiers accèdent aux données sans dépendre des data engineers.
- **Réduction des silos** : L’ontologie métier unifie les terminologies disparates.
- **Conformité** : Les métadonnées enrichies permettent de tracer l’origine des données.

---
### **LLM-as-a-Judge : l’auto-évaluation à l’échelle**
Netflix a déployé un système d’évaluation automatisé basé sur le concept de **"LLM-as-a-Judge"**, où un second modèle juge la qualité des sorties d’un premier modèle. Leur approche combine **Human-in-the-loop** et **monitoring continu** pour éviter la dérive des modèles.
→ [Lire l’article](https://netflixtechblog.medium.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508)

**Pourquoi c’est critique ?**
- **Scalabilité** : Impossible d’évaluer manuellement des millions de sorties.
- **Fiabilité** : Les modèles juges doivent être alignés sur les attentes humaines.
- **Réduction des coûts** : Moins de dépendance aux experts métiers pour la validation.

---
### **AML Investigations : suivre l’argent au-delà des alertes**
Neo4j explique comment les **graphes de connaissances** permettent de reconstruire des réseaux de blanchiment d’argent comme l’**Azerbaijani Laundromat**, impossible à détecter avec des systèmes traditionnels. Leur approche transforme les données transactionnelles en **intelligence contextuelle**.
→ [Lire l’article](https://neo4j.com/blog/fraud-detection/aml-investigations-following-suspicious-activity-beyond-the-alert/)

**Pourquoi c’est critique ?**
- **Conformité AML** : Les banques doivent prouver qu’elles traquent les flux suspects.
- **Réduction des faux positifs** : Les graphes permettent de contextualiser les alertes.
- **Collaboration inter-services** : Les équipes de conformité et de data science travaillent sur les mêmes données.

---
---

## **4. 💻 Agent Développeur & Développeur Augmenté**

### **GitHub Copilot SDK pour Java : l’IA dans l’IDE d’entreprise**
GitHub a lancé un **SDK Java** pour intégrer Copilot dans des applications d’entreprise, avec support du **BYOK (Bring Your Own Key)** pour utiliser des modèles hébergés sur Azure, Anthropic ou d’autres endpoints. Conçu pour le Java moderne (Jakarta EE 11, Spring), il tire parti des **threads virtuels** pour garantir la scalabilité.
→ [Lire l’article](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)

**Pourquoi c’est critique ?**
- **Gouvernance des modèles** : Les banques peuvent choisir où leurs données sont traitées.
- **Intégration transparente** : Les développeurs utilisent Copilot sans changer d’IDE.
- **Scalabilité** : Les threads virtuels permettent de gérer des milliers de requêtes simultanées.

---
### **Claude Code : la revue de code à l’ère de l’IA**
L’équipe de **Claude Code** partage sa méthodologie pour gérer la revue de code généré par des agents à haut volume. Leur approche repose sur :
- **Une couverture de tests rigoureuse** pour minimiser les régressions.
- **Un ciblage humain stratégique** pour les zones à haut risque.
→ [Lire l’article](https://claude.dev/blog/solving-code-review-at-anthropic/)

**Pourquoi c’est critique ?**
- **Productivité vs. Qualité** : L’IA accélère le codage, mais la revue reste un goulot d’étranglement.
- **Réduction de la dette technique** : Les revues automatisées détectent les patterns dangereux.
- **Culture d’ingénierie** : Les développeurs doivent apprendre à superviser l’IA.

---
### **JetBrains Air Governance : contrôler les agents dans l’IDE**
JetBrains lance **Air Governance**, une plateforme pour superviser l’usage des agents IA (Claude, Codex) dans les IDEs. Elle permet de :
- Définir des **politiques d’accès** (quels modèles sont autorisés).
- Piloter les **budgets** (coût par développeur).
- Analyser l’**impact sur la productivité**.
→ [Lire l’article](https://blog.jetbrains.com/ai/2026/11/livestream-scaling-agentic-development-with-air-governance/)

**Pourquoi c’est critique ?**
- **Gouvernance centralisée** : Les DSI veulent contrôler l’adoption de l’IA.
- **Optimisation des coûts** : Les modèles premium (Claude Sonnet 4.5) ont un coût élevé.
- **Alignement avec les processus DevOps** : Les agents doivent s’intégrer aux pipelines CI/CD.

---
### **Qodo’s Software Map : cartographier les dépendances pour mieux reviewer**
Qodo introduit une **vue dynamique des dépendances** entre services, permettant d’identifier :
- Les **zones de risque** avant un déploiement.
- Les **clusters de problèmes** détectés lors des revues de code.
→ [Lire l’article](https://www.qodo.ai/blog/10-ways-qodos-software-map-changes-how-your-team-reviews-plans-and-ships/)

**Pourquoi c’est critique ?**
- **Réduction des incidents** : Les équipes voient l’impact d’un changement avant de le commiter.
- **Documentation vivante** : La carte est synchronisée avec le code source.
- **Collaboration inter-équipes** : Les PO, devs et ops partagent la même vision.

---
### **Agentic Skill Decay : l’IA menace-t-elle l’expertise technique ?**
Addy Osmani alerte sur le **"Skill Decay"** : si les agents IA boostent la productivité immédiate, ils risquent d’**éroder la compréhension profonde des systèmes** par les développeurs. Une dépendance excessive aux outils automatisés pourrait rendre le débogage complexe et la maintenance difficile.
→ [Lire l’article](https://addyosmani.com/blog/agentic-skill-decay/)

**Pourquoi c’est critique ?**
- **Résilience à long terme** : Les banques ont besoin de développeurs capables de comprendre le code legacy.
- **Formation continue** : Les équipes doivent être formées à superviser l’IA, pas à la subir.
- **Équilibre humain-IA** : L’IA doit assister, pas remplacer, le jugement humain.

---
### **Brownfield Agentic Engineering : moderniser le legacy sans tout casser**
Addy Osmani propose une approche pragmatique pour intégrer des agents développeurs dans des **bases de code legacy**. La clé ? Fournir un **contexte riche** aux agents (via RAG ou indexation précise) pour naviguer dans des architectures documentées de manière obsolète.
→ [Lire l’article](https://addyosmani.com/blog/brownfield-agentic-engineering/)

**Pourquoi c’est critique ?**
- **Dette technique massive** : Les banques ont des systèmes vieillissants critiques.
- **Risque opérationnel** : Un agent mal configuré peut casser des processus métiers.
- **Migration progressive** : Il faut moderniser sans interruption de service.

---
### **Beyond the Hallucination : pourquoi l’IA a besoin de maths déterministes**
Capital One démontre que les modèles d’IA, de nature probabiliste, **ne peuvent pas être utilisés seuls** pour des calculs financiers exigeant une précision absolue. Leur architecture hybride associe :
- Une **couche de découverte par l’IA** (classification, NLP).
- Une **couche de calcul déterministe** (agrégations, vérifications).
→ [Lire l’article](https://medium.com/capital-one-tech/beyond-the-hallucination-why-ai-needs-deterministic-math-aa9c448479ab)

**Pourquoi c’est critique ?**
- **Fiabilité des données** : Les erreurs de calcul peuvent coûter des millions.
- **Conformité réglementaire** : Les régulateurs exigent des preuves de traçabilité.
- **Architecture robuste** : L’IA ne doit pas être une boîte noire pour les métiers.

---
---

## **5. 🏦 IA & Métiers Bancaires : Retail, Asset Management & CIB**

L’adoption de l’IA dans les institutions financières dépasse désormais le stade des démonstrateurs génériques pour s’ancrer au cœur des chaînes de valeur des trois piliers bancaires : **la Banque de Détail (Retail Banking)**, **la Gestion d’Actifs (Asset Management)** et **la Banque de Financement et d’Investissement (Corporate & Investment Banking - CIB)**.

---

### **A. Retail Banking (Banque de Détail) : De l'automatisation de masse à l'hyper-personnalisation en temps réel**

En banque de détail, la volumétrie massive de transactions et de clients impose une convergence étroite entre modèles d'IA probabilistes (LLM/SLM), moteurs de décision déterministes et intégration temps réel au Core Banking.

1. **Scoring de crédit instantané & Octroi augmenté** :
   - *Architecture* : Remplacement des grilles de scoring statiques par des modèles hybrides combinant Gradient Boosting (XGBoost/LightGBM) et modèles fondation entraînés sur les flux transactionnels DSP2 (Open Banking). Le moteur intègre des couches d'explicabilité intrinsèque (**SHAP** / **LIME**) pour satisfaire aux exigences strictes de transparence de l'**EU AI Act** (catégorie haut risque).
   - *Impact opérationnel* : Réduction du temps de décision d'octroi de 4 jours ouvrés à **moins de 3 minutes** pour les prêts personnels et crédits conso, avec une baisse de **18 % des défauts de paiement** grâce à une détection plus fine des micro-signaux de fragilité budgétaire.

2. **Agents conversationnels KYC & Conseiller bancaire augmenté** :
   - *Architecture* : Déploiement d'agents multimodaux capables d'effectuer l'analyse documentaire en direct (vérification biométrique faciale, conformité des pièces d'identité, extraction et validation d'avis d'imposition via OCR augmenté et vision). Côté conseiller en agence, l'agent agit comme un copilote "Next Best Action" qui synthétise l'historique 360° du client et suggère les produits d'épargne ou d'assurance les plus adaptés au profil de risque.
   - *Impact opérationnel* : Réduction de **65 % du temps consacré aux revues périodiques KYC** et automatisation de 45 % des demandes courantes de service client sans rupture de conformité.

3. **Détection de fraude transactionnelle ultra-rapide (Virements instantanés & CB)** :
   - *Architecture* : Utilisation de **Graph Neural Networks (GNN)** et de pipelines de streaming Apache Kafka / Apache Flink pour analyser la topologie des réseaux de paiement en **moins de 40 millisecondes**. Les fraudes sophistiquées (fraude au président, réseaux de blanchiment, mules bancaires) sont interceptées avant l'exécution du virement instantané SEPA.
   - *Gouvernance & DORA* : Résilience opérationnelle garantie par des topologies d'inférence redondées localement et supervision humaine des seuils de blocage.

---

### **B. Asset Management (Gestion d'Actifs) : Du signal faible à la thèse d'investissement augmentée**

Dans la gestion d'actifs et de fortune, l'IA agit comme un amplificateur d'intelligence pour les gérants de portefeuille et analystes financiers face à une explosion de données non structurées.

1. **Recherche augmentée (GraphRAG) sur données financières hétérogènes** :
   - *Architecture* : Pipeline GraphRAG connectant en continu les dépôts réglementaires (SEC 10-K, 10-Q, prospectus AMF), les earnings calls transcripts (audio transcrit via Whisper/Mistral Voxtral), les dépêches de presse (Bloomberg, Reuters) et les publications macroéconomiques. Les entités (entreprises, filiales, dirigeants, dettes, fournisseurs) sont reliées dans un graphe de connaissances sémantique.
   - *Impact opérationnel* : Un analyste peut interroger le corpus en langage naturel (*"Quels sont les risques supply chain mentionnés par les équipementiers automobiles européens dans leurs derniers trimestriels ?"*) et obtenir une note de synthèse sourcée en **30 secondes**, divisant par 5 le temps de revue pré-comité d'investissement.

2. **Génération de thèses d'investissement & Stress-testing macroéconomique** :
   - *Architecture* : Combinaison de SLM financiers spécialisés et de modèles d'optimisation quantitative (Black-Litterman, Monte Carlo). L'agent formule des scénarios contrefactuels (*"Hausse des taux de la BCE de 50 bps conjuguée à un choc pétrolier"*) et projette l'impact dynamique sur les corrélations d'actifs et la VaR (Value at Risk) du portefeuille.
   - *Impact opérationnel* : Réactivité accrue lors des chocs de marché et rééquilibrage préventif des portefeuilles gérés sous mandat.

3. **Conformité ESG & Détection du Greenwashing** :
   - *Architecture* : Confrontation automatisée des déclarations textuelles des émetteurs (rapports RSE, CSRD, SFDR Article 8/9) avec des métriques réelles tierces (données satellitaires d'émissions de méthane, amendes environnementales, alertes ONG).
   - *Impact opérationnel* : Sécurisation de la classification des fonds durables et élimination des risques de sanction par les régulateurs européens (ESMA).

---

### **C. Corporate & Investment Banking (CIB) : Automatisation des flux complexes et modélisation des risques de marché**

La banque de financement et d'investissement se caractérise par des transactions sur mesure, des volumes de contrats juridiques titanesques et des besoins de calcul intensif en salle des marchés.

1. **Structuration de Deals M&A & Syndication de Crédits (LMA standard)** :
   - *Architecture* : Agents d'analyse contractuelle spécialisés dans le droit financier et les standards de la *Loan Market Association* (LMA). L'agent ingère des contrats de plusieurs centaines de pages, extrait automatiquement les **covenants financiers** (leverage ratios, interest cover), les clauses de changement de contrôle (*change-of-control*) et les conditions préalables (*conditions precedent*), tout en produisant une matrice de conformité auditable.
   - *Impact opérationnel* : Réduction de **70 % du temps d'audit contractuel** lors des due diligences M&A, permettant aux banquiers conseils de sécuriser les closing plus rapidement et de limiter les risques de contentieux.

2. **Pricing de dérivés complexes & Accélération des simulations de risque (Deep XVA)** :
   - *Architecture* : Remplacement des simulations Monte Carlo traditionnelles exécutées sur d'immenses fermes de serveurs nocturnes par des réseaux neuronaux profonds entraînés à reproduire les surfaces de volatilité et les ajustements d'évaluation (CVA/DVA/FVA).
   - *Impact opérationnel* : Le calcul des XVA sur des portefeuilles de dérivés exotiques passe de **plusieurs heures à quelques dizaines de millisecondes**, permettant un pricing intra-day en direct pendant la négociation avec les clients corporate.

3. **Surveillance des marchés & Détection d'abus (Règlement MAR)** :
   - *Architecture* : Corrélation multimodale temps réel entre les flux d'ordres (FIX protocol), les enregistrements vocaux des traders (speech-to-text sécurisé), les messageries instantanées professionnelles et les flux d'actualités.
   - *Impact opérationnel* : Détection proactive des comportements anormaux (spoofing, layering, front-running, manipulation d'indices de référence) avec une réduction de **80 % des faux positifs** traités par les équipes de conformité.

4. **Automatisation post-trade & Réconciliation des transactions** :
   - *Architecture* : Agents intelligents de réconciliation tripartite (banque, contrepartie, dépositaires centraux Euroclear/DTCC) appliquant la norme **ISO 20022**. L'agent analyse la cause racine des rejets d'ordres (*trade breaks*) et propose automatiquement les écritures correctives.
   - *Impact opérationnel* : Diminution drastique des pénalités de règlement sous le régime européen **CSDR** et fluidification des règlements-livraisons.

---
---

## **📊 L’Infographie Technique de la Semaine**

![Bar chart, Agent B before the schema fix, 36 runs per model. Schema-valid output: 30 of 36 on Gemini 3.5 Flash, 36 of 36 on Gemini 3.8 Flash. Cases matching the oracle: 12 and 13 of 36. Mean field-match score: 0.40 for both.](https://cdn-images-1.medium.com/max/1024/1*JqF2NPBn5wFn8E5h6Y_Gag.png)

**Analyse pour un grand groupe bancaire :**

### **Contexte & Architecture**
Cette infographie provient d’un article de **Google Cloud** sur l’évaluation des modèles d’IA ([lien](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e)). Elle compare les performances de deux modèles (Gemini 3.5 Flash et 3.8 Flash) avant et après une correction de schéma.

- **Composants clés** :
  - **Agent B** : Un agent IA évaluant des sorties de modèle.
  - **Schémas de validation** : Vérification de la structure des données générées.
  - **Oracle** : Une vérité de référence pour mesurer la précision.
  - **Mean field-match score** : Métrique de correspondance entre les sorties et l’oracle.

### **Enjeux pour nos projets**
1. **Fiabilité des sorties IA** :
   - Les modèles d’IA génèrent souvent des données **non conformes aux schémas métiers** (ex : JSON mal formaté, champs manquants).
   - **Solution** : Intégrer des **garde-fous déterministes** (Pydantic, JSON Schema) avant toute utilisation en production.

2. **Observabilité GenAI** :
   - Le **Mean field-match score** est une métrique clé pour mesurer la qualité des sorties.
   - **Application bancaire** : Pour les agents générant des rapports financiers ou des contrats, cette métrique doit être **monitorée en temps réel**.

3. **Passage à l’échelle sur GCP/IBM Cloud** :
   - Google Cloud propose des outils comme **Vertex AI** pour déployer ces modèles à l’échelle.
   - **Recommandation** : Utiliser des **workflows serverless** (Cloud Functions, Cloud Run) pour valider les sorties IA avant leur ingestion dans les systèmes critiques.

4. **FinOps & Coûts** :
   - Les appels répétés à l’IA pour corriger des erreurs de schéma **augmentent les coûts**.
   - **Optimisation** : Pré-validations locales avant envoi au modèle.

### **Enseignements opérationnels**
- **Ne pas faire confiance aveuglément aux LLM** : Toujours valider les sorties avec des **tests déterministes**.
- **Automatiser l’évaluation** : Utiliser des **pipelines CI/CD** pour tester les modèles avant déploiement.
- **Former les équipes** : Les développeurs doivent comprendre les **limites des modèles** et les **bonnes pratiques de validation**.

---
---

## **🗺️ La Carte Stratégique (Wardley Map) de la Semaine**

![Wardley Map - A good enough map](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdDK7_kvC0fkbYJNouIDIUHo0yfvBugq5bKMmUxavEs3YKYzMNHZok1ibhTtU4jGlaRGeElExA0dVfmajAKTQHNdZJFaQbzx3RgYnMX3z2I0q9KX5ITL5ViB6f6LoXYv2aCslodOxxKJXmZdq0EeL6TBFMWUO-frYqS-M3UDfMe5JgLiodljA1Rg/w400-h145/map04.png)

**Source** : [Simon Wardley - A good enough map](https://blog.gardeviance.org/2024/02/a-good-enough-map.html)

### **Analyse stratégique pour un grand groupe bancaire**

#### **1. Chaîne de valeur (axe vertical)**
- **Utilisateur final** : Besoin de **processus métiers standardisés** et **conformes**.
- **Processus métier** : Standardisation des procédures (ex : KYC, AML).
- **Outils & Plateformes** : Solutions d’IA (Amazon Bedrock, watsonx.data).
- **Infrastructure** : Cloud (AWS, GCP, Azure), bases de données (Neptune, FSx for ONTAP).

#### **2. Évolution des composants (axe horizontal)**
| **Composant**               | **Position sur l’axe** | **Stratégie recommandée**                          |
|-----------------------------|-------------------------|----------------------------------------------------|
| **Processus métier**        | Produit → Commodité     | Automatiser avec l’IA (ex : MUFG Bank).           |
| **Ontologies métier**       | Sur mesure → Produit    | Industrialiser via Amazon Neptune/Bedrock.         |
| **Agents IA**               | Genèse → Sur mesure     | Développer des garde-fous (ex : validation déterministe). |
| **Cloud Infrastructure**    | Commodité               | Choisir des fournisseurs souverains (GCP, IBM).    |
| **Observabilité**           | Produit → Commodité     | Utiliser OpenTelemetry et des outils comme Instana.|

#### **3. Mouvements stratégiques**
- **Commoditisation de l’inférence** :
  Les modèles LLM deviennent des **commodités** (ex : Bedrock, Vertex AI). Les banques doivent se concentrer sur **l’orchestration** et la **gouvernance**, pas sur l’entraînement de modèles.

- **Industrialisation des ontologies** :
  Les graphes de connaissances (Neo4j, Amazon Neptune) passent de **sur mesure** à **produit**, permettant une **standardisation à l’échelle**.

- **Gestion des dépendances** :
  Les équipes doivent éviter de **réinventer la roue** et privilégier des solutions managées (ex : watsonx.data pour le Text-to-SQL).

#### **4. Opportunités pour le Cloud (GCP/IBM Cloud)**
- **IBM Cloud** :
  - **watsonx.data** pour la gouvernance des données.
  - **OpenShift** pour les workloads hybrides.
- **GCP** :
  - **Vertex AI** pour le déploiement d’agents.
  - **BigQuery** pour l’analyse des logs d’IA.

#### **5. Inerties organisationnelles à surmonter**
- **Résistance au changement** : Les équipes métiers préfèrent souvent les **runbooks manuels**.
- **Complexité des architectures legacy** : Les systèmes monolithiques freinent l’adoption de l’IA.
- **Manque de compétences** : Les data engineers doivent monter en compétences sur les **graphes et l’ontologie**.

---
---

## **🚀 Projets Pilotes à Lancer sous 3 Mois**

### **🔹 Projet Pilote #1 : Standardisation des Processus Métiers par Ontologie (MUFG Bank Style)**
**Objectif** :
Valider que l’**ontologie métier + IA générative** peut réduire de **50 % le temps de développement** des procédures opérationnelles (ex : onboarding client, conformité AML) dans une équipe de 10 personnes.

**Périmètre équipe** :
- 2 développeurs backend (Java/Spring).
- 1 architecte cloud (AWS/GCP).
- 1 Product Owner (PO) métier (conformité bancaire).
- 1 data engineer (Neo4j/Amazon Neptune).
- 1 expert en gouvernance (RGPD, EU AI Act).

**Durée & Jalons** :
- **M1 (Mois 1)** :
  - Cartographier les processus métiers existants (ex : workflow KYC).
  - Déployer une ontologie de base dans **Amazon Neptune**.
  - Prototyper un agent IA générant des diagrammes de flux à partir de l’ontologie.
- **M2 (Mois 2)** :
  - Intégrer l’agent dans un **IDE d’entreprise** (ex : VS Code avec GitHub Copilot).
  - Tester la génération de procédures pour 3 cas d’usage réels.
  - Mesurer le temps de développement avant/après.
- **M3 (Mois 3)** :
  - Déployer en **pré-production** avec un groupe de testeurs métiers.
  - Former les équipes à l’utilisation de l’ontologie.
  - Présenter les résultats à la direction (ROI, réduction des coûts).

**Critères de succès** :
- Réduction de **30 % du temps de développement** des procédures.
- **100 % des procédures générées** conformes aux schémas métiers.
- **Feedback positif** de 80 % des testeurs métiers.

**Risques & Mitigation** :
- **Risque** : L’ontologie est incomplète ou mal modélisée.
  **Mitigation** : Impliquer un **expert métier** dès le début et valider avec des ateliers.
- **Risque** : Les agents génèrent des procédures incorrectes.
  **Mitigation** : Ajouter une **couche de validation humaine** avant déploiement.

---
### **🔹 Projet Pilote #2 : Agent Développeur Sécurisé dans un Environnement Bancaire (Capital One Style)**
**Objectif** :
Évaluer l’impact d’un **IDE agentique (Claude Code/GitHub Copilot)** sur la productivité d’une équipe de 10 développeurs, tout en garantissant la **sécurité et la conformité** du code généré.

**Périmètre équipe** :
- 4 développeurs backend (Java/Spring, Python).
- 2 développeurs frontend (React/TypeScript).
- 1 architecte sécurité (Zero Trust, mTLS).
- 1 expert DevOps (CI/CD, ArgoCD).
- 1 PO (alignement avec les besoins métiers).
- 1 data engineer (pour les tests automatisés).

**Durée & Jalons** :
- **M1 (Mois 1)** :
  - Configurer **JetBrains Air Governance** ou **GitHub Copilot Enterprise** dans l’IDE.
  - Définir des **politiques de sécurité** (ex : interdire l’accès aux données clients sensibles).
  - Former les équipes à l’utilisation de l’agent (prompts, revues de code).
- **M2 (Mois 2)** :
  - Lancer un **projet pilote** (ex : refonte d’un microservice existant).
  - Mesurer la **vélocité** (lignes de code générées vs. manuelles).
  - Automatiser les **revues de code** avec des outils comme **Qodo** ou **Sourcegraph Cody**.
- **M3 (Mois 3)** :
  - Déployer en **production limitée** (1 feature flag).
  - Analyser les **métriques de qualité** (nombre de bugs, dette technique).
  - Présenter un **bilan FinOps** (coût des appels API vs. gain de productivité).

**Critères de succès** :
- **Réduction de 40 % du temps de développement** pour les tâches répétitives.
- **0 régression majeure** liée au code généré.
- **Coût maîtrisé** : Moins de 10 % d’augmentation des coûts Cloud.

**Risques & Mitigation** :
- **Risque** : Le code généré contient des **vulnérabilités** (ex : injection SQL).
  **Mitigation** : Intégrer des **scanners de sécurité** (SonarQube, Snyk) dans le pipeline.
- **Risque** : Les développeurs **perdent en expertise**.
  **Mitigation** : Organiser des **ateliers de revue de code manuelle** pour valider les sorties IA.

---
### **🔹 Projet Pilote #3 : Observabilité GenAI avec IBM Instana & OpenTelemetry**
**Objectif** :
Déployer une **solution d’observabilité centrée IA** pour monitorer les coûts, performances et qualité des appels LLM dans un environnement bancaire.

**Périmètre équipe** :
- 2 SREs (Site Reliability Engineers).
- 1 architecte observabilité (OpenTelemetry, Prometheus).
- 1 expert FinOps (coût par token).
- 1 data engineer (pour les logs et métriques).

**Durée & Jalons** :
- **M1 (Mois 1)** :
  - Intégrer **IBM Instana GenAI Observability** dans le pipeline CI/CD.
  - Configurer **OpenTelemetry** pour collecter les métriques des appels LLM.
  - Définir des **alertes** pour les dérives de coût ou de qualité.
- **M2 (Mois 2)** :
  - Tester sur un **cas d’usage réel** (ex : assistant IA pour le service client).
  - Mesurer le **coût par token** et le **temps de réponse**.
  - Automatiser les **rapports FinOps** pour la direction.
- **M3 (Mois 3)** :
  - Déployer en **production** avec un dashboard centralisé.
  - Former les équipes à l’utilisation des outils.
  - Présenter un **bilan d’impact** (réduction des coûts, amélioration de la résilience).

**Critères de succès** :
- **Réduction de 20 % des coûts** liés aux appels LLM.
- **MTTR (Mean Time To Resolution)** réduit de 30 % pour les incidents liés à l’IA.
- **100 % des métriques** (coût, latence, qualité) visibles en temps réel.

**Risques & Mitigation** :
- **Risque** : La solution est trop complexe à déployer.
  **Mitigation** : Commencer par un **PoC limité** avant généralisation.
- **Risque** : Les métriques ne sont pas actionnables.
  **Mitigation** : Impliquer les **équipes FinOps et SRE** dès la conception.

---
### **🔹 Projet Pilote #4 : Migration Hybride Oracle Database vers AWS (avec FSx for ONTAP)**
**Objectif** :
Valider la migration d’une **Oracle Database critique** vers AWS avec **Amazon FSx for NetApp ONTAP**, en garantissant **zéro interruption de service** et une **réduction des coûts de 20 %**.

**Périmètre équipe** :
- 2 administrateurs base de données (DBA).
- 1 architecte cloud (AWS, VMware).
- 1 expert en reprise d’activité (DR).
- 1 PO (alignement avec les besoins métiers).

**Durée & Jalons** :
- **M1 (Mois 1)** :
  - Analyser les **dépendances** de la base Oracle existante.
  - Configurer **Amazon FSx for ONTAP** et tester les performances.
  - Planifier la **réplication inter-régions** (SnapMirror).
- **M2 (Mois 2)** :
  - Migrer un **sous-ensemble de données** en environnement de test.
  - Valider les **latences** et les **performances**.
  - Former les DBAs à la gestion de la nouvelle infrastructure.
- **M3 (Mois 3)** :
  - Basculer **10 % du trafic** en production limitée.
  - Mesurer les **coûts** (stockage, calcul) et les **performances**.
  - Présenter un **plan de généralisation** à la direction.

**Critères de succès** :
- **Latence < 1 ms** pour les transactions critiques.
- **Réduction de 20 % des coûts** de stockage et de sauvegarde.
- **0 incident majeur** pendant la migration.

**Risques & Mitigation** :
- **Risque** : Les performances ne sont pas au rendez-vous.
  **Mitigation** : Tester en **charge réelle** avant basculement.
- **Risque** : La reprise d’activité (DR) ne fonctionne pas.
  **Mitigation** : Simuler un **test de basculement complet** avant M3.

---
### **🔹 Projet Pilote #5 : Copilote d'Extraction & Audit Automatisé de Contrats CIB & Syndication (LMA Standard)**
**Objectif** :
Valider qu'un agent RAG spécialisé avec garde-fous déterministes peut extraire **100 % des covenants financiers** et clauses critiques de contrats de crédit syndiqué (norme LMA) de 150+ pages avec un taux d'exactitude **> 99 %**.

**Périmètre équipe** :
- 2 développeurs backend / IA (Python, LangChain, LlamaParse).
- 1 juriste financier senior CIB (expert documentation de financement).
- 1 architecte sécurité & conformité (Zero Trust, Cloud souverain).
- 1 data engineer (GraphRAG, Neo4j / Amazon Neptune).
- 1 Product Owner Financement Structuré / Syndication.

**Durée & Jalons** :
- **M1 (Mois 1)** :
  - Constitution du corpus d'évaluation (50 contrats de crédit syndiqué bilingues FR/EN anonymisés).
  - Mise en place du pipeline de parsing multimodal et de découpage sémantique respectant la structure LMA.
  - Modélisation de l'ontologie contractuelle (définition des ratios de levier, clauses *Negative Pledge*, *Change of Control*, *Events of Default*).
- **M2 (Mois 2)** :
  - Entraînement et raffinement des prompts avec extraction structurée (Pydantic / JSON Schema).
  - Double vérification déterministe liant chaque ratio extrait à la citation exacte et à la page source.
  - Benchmark aveugle face à l'audit manuel réalisé par l'équipe juridique CIB.
- **M3 (Mois 3)** :
  - Intégration dans le portail interne de deal execution CIB.
  - Déploiement auprès de 15 banquiers et juristes en conditions réelles de deal.
  - Présentation du bilan de conformité DORA / ACPR et calcul du ROI.

**Critères de succès** :
- **Réduction de 60 % du temps d'audit contractuel** lors des due diligences.
- **0 covenant critique omis** sur le corpus de test.
- Taux de satisfaction **> 90 %** des juristes et banquiers conseils.

**Risques & Mitigation** :
- **Risque** : Hallucination ou mauvaise interprétation de clauses rédigées sur mesure.
  **Mitigation** : Principe d'explicabilité stricte : l'interface surligne le texte original cliquable pour chaque champ extrait, maintenant un humain dans la boucle (*Human-in-the-loop* obligatoire pour tout closing).

---
---

## **🏢 Projets Réels Passés à l’Échelle**

### **[Netflix] : Ontology-Driven Observability – Un graphe de connaissances à l’échelle**
**Catégorie** : Architecture Évolutive & Ingénierie Logicielle

**Contexte & Verrou Initial** :
Netflix gère **des milliers de microservices** distribués, ce qui rend le diagnostic des incidents **extrêmement complexe**. Les outils traditionnels (logs, métriques, traces) ne suffisent plus pour comprendre les **dépendances entre services**.

**Architecture & Déploiement** :
- **Graphe de connaissances** : Modélisation explicite des relations entre services (ex : dépendances, flux de données).
- **Ontologie** : Définition des concepts métiers (ex : "service critique", "flux financier").
- **Échelle** : Des **millions de nœuds** et d’arêtes, avec une latence de requête < 100 ms.
- **Outils** : Utilisation de **Neo4j** pour le stockage et **Apache Kafka** pour les flux de données.

**Impact Chiffré & Résultats** :
- **Réduction du MTTR** : Passage de **plusieurs heures** à **quelques minutes** pour résoudre les incidents.
- **Amélioration de la résilience** : Détection précoce des **points de défaillance uniques**.
- **Documentation vivante** : La carte est **automatiquement synchronisée** avec le code source.

**Référence Publique** :
[Netflix Tech Blog – Ontology-Driven Observability](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf)

---
### **[Capital One] : Beyond the Hallucination – Architecture Hybride IA + Maths Déterministes**
**Catégorie** : Data & Agentic AI

**Contexte & Verrou Initial** :
Capital One utilise des **LLMs pour classer des documents financiers** (ex : relevés bancaires), mais les erreurs de classification peuvent avoir un **impact réglementaire ou financier majeur**. Les modèles probabilistes ne garantissent pas une **précision absolue**.

**Architecture & Déploiement** :
- **Couche IA** : Utilisation de **LLMs** pour extraire des entités et classer les documents.
- **Couche déterministe** : Validation des résultats avec des **règles métiers** (ex : sommes cohérentes, formats attendus).
- **Échelle** : Traitement de **millions de documents par jour** avec un **temps de réponse < 500 ms**.
- **Outils** : **IBM watsonx.data** pour la gouvernance, **FastAPI** pour l’exposition des services.

**Impact Chiffré & Résultats** :
- **Réduction des erreurs** : Passage de **5 % d’erreurs** à **< 0,1 %**.
- **Conformité renforcée** : Preuves de traçabilité pour les régulateurs.
- **Gain de productivité** : Les analystes passent **80 % de leur temps** sur l’analyse plutôt que sur la correction.

**Référence Publique** :
[Capital One Tech – Beyond the Hallucination](https://medium.com/capital-one-tech/beyond-the-hallucination-why-ai-needs-deterministic-math-aa9c448479ab)

---
### **[GitHub] : Nouvelle Architecture de Stockage Git – Prête pour l’Ère des Agents**
**Catégorie** : Rationalisation & Simplification du SI

**Contexte & Verrou Initial** :
GitHub doit gérer **des milliers d’écritures par seconde** et des **lectures à la demande** pour supporter l’échelle des agents de développement. L’ancienne architecture était un **goulot d’étranglement**.

**Architecture & Déploiement** :
- **Découplage stockage/calcul** : Réplicas virtuels sur **Azure Blob Storage**.
- **Minimisation de la coordination** : Écritures optimisées pour réduire les latences.
- **Échelle** : Support de **millions de dépôts** avec une **latence < 100 ms**.
- **Outils** : **Spokes** (système interne de GitHub) pour la gestion des écritures.

**Impact Chiffré & Résultats** :
- **Réduction des latences** : Passage de **plusieurs secondes** à **< 100 ms** pour les lectures.
- **Scalabilité horizontale** : Possibilité d’ajouter des nœuds **sans interruption**.
- **Préparation pour l’IA** : Infrastructure prête pour les **agents de codage autonomes**.

**Référence Publique** :
[GitHub Engineering – Inside GitHub’s new Git storage architecture](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/)

---
### **[MUFG Bank] : AI Flowchart – Réduction de 90 % du Temps de Développement des Procédures**
**Catégorie** : Agent Développeur & Développeur Augmenté

**Contexte & Verrou Initial** :
MUFG Bank avait **30 000 procédures opérationnelles** dispersées dans **30 pays**, avec des **duplications massives** et des **risques de non-conformité**. La documentation manuelle était **obsolète et inefficace**.

**Architecture & Déploiement** :
- **Ontologie métier** : Modélisation des processus dans **Amazon Neptune**.
- **IA générative** : Utilisation d’**Amazon Bedrock** pour générer des diagrammes de flux à partir de l’ontologie.
- **Échelle** : Déploiement dans **100+ succursales** avec une **réduction du temps de développement** de 11 à 1 jour/homme.
- **Outils** : **Amazon Bedrock Knowledge Bases** pour le RAG, **Guardrails** pour la modération.

**Impact Chiffré & Résultats** :
- **Réduction de 90 % du temps de développement** des procédures.
- **Standardisation globale** : **100 % des procédures** conformes aux schémas métiers.
- **Gain de conformité** : Réduction des **risques réglementaires** liés aux processus fragmentés.

**Référence Publique** :
[AWS Neptune Database Blog – MUFG Bank Case Study](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

---
### **[JPMorgan Chase] : LLM Suite & COiN – L'IA Générative en Production pour CIB et Asset Management**
**Catégorie** : IA & Métiers Bancaires (Retail, Asset Management & CIB)

**Contexte & Verrou Initial** :
L'analyse manuelle des contrats de crédit syndiqué, prospectus d'émission et accords de dérivés consommait plus de 360 000 heures de juristes et banquiers d'affaires chaque année, avec un risque d'erreur humaine et une lenteur dans l'exécution des transactions de marché.

**Architecture & Déploiement** :
- **Plateforme interne unifiée** : Déploiement de *LLM Suite*, une plateforme d'IA générative hébergée sur cloud privé sécurisé, intégrée à *COiN* (*Contract Intelligence*) et aux systèmes transactionnels CIB et Asset Management.
- **Garde-fous stricts** : Isolation complète des données de marché et clients, zéro rétention des prompts côté fournisseurs de modèles, traçabilité cryptographique et journalisation pour la conformité SEC et FINRA.
- **Échelle** : Déploiement auprès de plus de **200 000 collaborateurs** du groupe, dont plus de 60 000 banquiers d'affaires, analystes de recherche et gérants d'actifs.

**Impact Chiffré & Résultats** :
- **Extraction de 150 attributs financiers clés** à partir de contrats de crédit en **quelques secondes** (au lieu de plusieurs heures par contrat).
- **Économie de 360 000 heures de travail juridique par an**, réorientées vers la négociation à forte valeur ajoutée.
- **Accélération des notes de recherche** en Asset Management : réduction de 75 % du temps de synthèse des conférences de résultats financiers (*earnings calls*).

**Référence Publique** :
[JPMorgan Chase Investor & Tech Day – AI & Contract Intelligence (COiN) in Production](https://www.jpmorganchase.com/news-stories/technology-and-innovation-at-jpmorgan-chase)
---

## **🎯 Conclusion : Vers une Ingénierie Logicielle "Agent-Native"**

Cette semaine de veille a révélé une **accélération sans précédent** dans l’adoption de l’IA agentique, mais aussi des **défis majeurs** en termes de gouvernance, de coût et de résilience.

**Les 3 enseignements clés pour BNP Paribas :**
1. **L’IA n’est plus un outil, mais un acteur** : Les agents autonomes transforment nos processus, nos architectures et nos compétences. Il faut **repenser la gouvernance** (FinOps, sécurité, conformité) pour éviter les dérives.
2. **La rationalisation est un impératif** : Les architectures legacy et les processus fragmentés sont incompatibles avec l’ère de l’IA. Les ontologies, les graphes de connaissances et les plateformes managées (AWS, GCP, IBM) sont des **levier de simplification**.
3. **Le développeur augmenté est une réalité** : Les IDEs agentiques (GitHub Copilot, Claude Code) et les outils de revue automatisée (Qodo, Sourcegraph) **changent la donne**. Mais ils exigent une **nouvelle culture d’ingénierie**, où l’humain supervise l’IA, pas l’inverse.

**Question ouverte pour la discussion :**
*Comment concilier l’urgence de l’innovation IA avec la rigueur des processus bancaires ? Faut-il privilégier des pilotes "shadow IT" pour tester rapidement, ou une approche centralisée et gouvernée dès le départ ?*

---
**📌 Partagez vos retours en commentaires ou en message privé !**
*Quels projets pilotes vous semblent les plus pertinents pour BNP Paribas ?*
*Quels sont les freins que vous anticipez dans l’adoption de l’IA agentique ?*