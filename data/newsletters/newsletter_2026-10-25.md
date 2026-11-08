# 🏛️ Architecture d'Entreprise Weekly

*Par le Bureau d'Architecture d'Entreprise — Veille Technologique & Stratégique SI*

Chères équipes, chers collègues,

Cette semaine, la veille technologique s'articule autour d'un constat sans appel : **l'ère de la découverte créative de l'IA fait place à l'exigence de maîtrise industrielle, budgétaire et sécuritaire.** Alors que le coût du "premier diff" s'effondre avec la génération automatisée de code, la véritable charge transférée sur le Système d'Information réside désormais dans la gouvernance du contexte, la revue critique du code et la maîtrise du *TCO (Total Cost of Ownership)* applicatif. 

Entre l'émergence des architectures d'agents autonomes à **autonomie graduée**, la bascule des protocoles d'intégration IA vers le **stateless**, et la nécessité d'une **résilience active** face au risque de dégradation des services Cloud et LLM, notre trajectoire d'architecture doit allier pragmatisme et rigueur d'ingénierie.

Bonne lecture !

---

## 1. 🔄 Rationalisation & Simplification du SI

Le principal défi de modernisation des grands groupes financiers ne réside pas dans l'adoption de nouvelles technologies, mais dans notre capacité à faire évoluer les modèles opérationnels et les infrastructures d'accueil sans y plaquer des réflexes "legacy".

* **Dépasser le biais de transposition "Legacy sur le Cloud"** : Dans son billet [*The digital grass isn’t greener. It isn’t grass.*](https://architectelevator.com/transformation/digital-grass-greener/), Gregor Hohpe met en garde contre l'erreur classique consistant à projeter nos contraintes de contrôle traditionnelles sur le Cloud et le numérique. Pour les banques, la transformation numérique exige de revoir la nature même des coûts et des arbitrages de gouvernance plutôt que de recréer des silos d'approbation sur des architectures modernes.
* **La résilience active face à la dérive d'architecture** : Microsoft Azure souligne dans [*Your architecture diagram is not your resilience*](https://azure.microsoft.com/en-us/blog/your-architecture-diagram-is-not-your-resilience/) que la résilience d'un SI n'est pas un état théorique figé sur un schéma, mais une propriété dynamique à tester en continu. Avec l'intégration des dépendances IA (API d'inférence, pipelines RAG), les systèmes doivent être conçus pour fonctionner sereinement même en cas d'indisponibilité ou d'hallucination d'un modèle d'IA partenaire.
* **Souveraineté Numérique et Cloud Bancaire** : AWS formalise son [*Digital Sovereignty Lens for the Well-Architected Framework*](https://aws.amazon.com/blogs/architecture/announcing-the-aws-digital-sovereignty-well-architected-lens/), structuré autour de 5 piliers : localisation des données, contrôles d'accès, continuité d'activité, portabilité et auditabilité. Un cadre essentiel pour nos arbitrages d'hébergement hybride.
* **FinOps & Efficience au niveau matériel** : Cloudflare démontre dans [*Saving another 100TB of RAM with math (and Rust)*](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/) et [*DNS Cache Memory Optimization*](https://blog.cloudflare.com/dns-cache-memory-optimization-1111/) qu'une réingénierie algorithmique bas niveau (hachage cohérent, structures Rust) permet d'économiser des centaines de téraoctets de RAM. De son côté, Netflix partage [*Stratum Container Right-Sizing*](https://netflixtechblog.medium.com/netflix-stratum-media-processing-automated-container-right-sizing-ddf9aa68a801?source=rss-c3aeaf49d8a4------2), un système automatisé d'ajustement dynamique de la mémoire et du CPU pour lutter contre le surdimensionnement précautionneux des conteneurs.

---

## 2. 🏗️ Architecture Évolutive & Ingénierie Logicielle

La prolifération du code généré par IA déplace le goulot d'étranglement de l'ingénierie logicielle du *codage* vers la *revue de code* et la *gestion du contexte*.

* **Le pattern AI Gateway pour découpler les évolutions LLM** : InfoQ présente dans [*An Evolutionary Architecture Pattern for Managing AI’s Pace of Change*](https://www.infoq.com/articles/evolutionary-architecture-pattern/) le rôle central des AI Gateways. Ce pattern permet de centraliser le routage sémantique, le filtrage de sécurité et l'auditabilité sans impacter les composants applicatifs métier.
* **MCP Stateless : Simplification majeure de la scalabilité** : AWS Architecture analyse la mise à jour majeure du [*Model Context Protocol (MCP went stateless)*](https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/). En supprimant la gestion d'état de session du protocole de base, les architectures d'agents éliminent les *sticky sessions* et s'intègrent désormais sur de simples passerelles de routage horizontales (Round-Robin). Luca Rossi détaille également les bonnes pratiques de conception dans [*How to Design a Good MCP Server*](https://refactoring.fm/p/how-to-design-a-good-mcp-server/).
* **Le coût de la revue de code à l'ère des LLM** : GitHub Engineering analyse le déplacement des coûts d'ingénierie dans [*The cost of saying yes has changed*](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/) et [*Better tools made Copilot code review worse*](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/). Alors qu'écrire une première version ne coûte plus rien, le vrai critère d'arbitrage humain reste le coût de propriété à long terme (sécurité, conformité, maintenance). GitHub a d'ailleurs réduit de 20% ses coûts de revue automatisée en restreignant l'accumulation inutile de contexte pour imiter la focalisation ciblée d'un réviseur humain.
* **Observabilité en temps réel et résilience des dépendances** : Netflix partage son retour d'expérience sur la cartographie dynamique de topologie de services via flux eBPF et Kafka dans [*Building Service Topology at Scale*](https://netflixtechblog.com/building-service-topology-at-scale-architecture-challenges-and-lessons-learned-f4b792f3f0d8?source=rss-c3aeaf49d8a4------2), en insistant sur la contre-pression réactive (*reactive backpressure*) pour protéger les systèmes lors d'incidents majeurs.

---

## 3. 🧠 Data & Agentic AI

L'IA agentique passe du statut de gadget conversationnel à celui de système distribué autonome réclamant une rigueur d'ingénierie équivalente à celle des systèmes transactionnels.

* **La "Taxe de l'Orchestrateur" et le découplage du contexte** : Dans [*The Orchestrator's Tax*](https://martinfowler.com/articles/orchestrator-tax.html), Martin Fowler rappelle que l'intérêt principal d'une architecture multi-agents n'est pas uniquement le parallélisme d'exécution, mais la protection de la fenêtre de contexte (*context window*) de l'orchestrateur principal contre la surcharge cognitive.
* **Confiance et Autonomie Graduée** : AWS Architecture formalise le framework [*Closing the AI agent trust gap with graduated autonomy*](https://aws.amazon.com/blogs/architecture/closing-the-ai-agent-trust-gap-with-graduated-autonomy/). Au lieu de donner des accès binaires (tout ou rien) aux agents autonomes, le système leur attribue des permissions dynamiques basées sur leur niveau de fiabilité mesuré et la réversibilité de leurs actions.
* **Plateformes Agent-First et Gestion de l'Identité** : Microsoft introduit le concept de plateformes *Agent-First* dans [*Designing agent-first platforms*](https://azure.microsoft.com/en-us/blog/designing-agent-first-platforms-what-changes-when-agents-do-the-work/), reposant sur Entra Agent ID pour doter les agents d'une identité propre, vérifiable et auditable dans les journaux d'entreprise.
* **Rattacher l'IA au déterministe et au contextuel** : Capital One rappelle dans [*Beyond the hallucination: Why AI needs deterministic math*](https://medium.com/capital-one-tech/beyond-the-hallucination-why-ai-needs-deterministic-math-aa9c448479ab?source=rss----3db3a67cb648---4) que l'IA probabiliste ne doit jamais exécuter directement de calculs financiers. La bonne architecture entoure le LLM de *wrappers déterministes*. En parallèle, Neo4j démontre dans [*What is contextual retrieval?*](https://neo4j.com/blog/agentic-ai/contextual-retrieval/) l'apport des graphes de connaissances (GraphRAG) pour alimenter la mémoire long terme et la traçabilité de décision des agents.
* **Industrialisation de l'évaluation (LLM-as-a-Judge)** : Netflix détaille son framework complet d'évaluation en continu dans [*The Lifecycle of LLM-as-a-Judge*](https://netflixtechblog.medium.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508?source=rss-c3aeaf49d8a4------2), en insistant sur la boucle de rétroaction humaine (*Human-in-the-Loop*) pour éviter le dérive silencieuse des modèles juges.

---

## 📊 L'Infographie Technique de la Semaine

![Running Apache Spark Jobs on IBM watsonx.data](https://cdn-images-1.medium.com/max/1024/1*iEnJfBaAgT9D6-V7aF5WxQ.png)
*Source : [IBM Data & watsonx — Running Apache Spark Jobs on IBM watsonx.data](https://medium.com/ibm-data-ai/running-apache-spark-jobs-on-ibm-watsonx-data-1467f3b7b1f0?source=rss----59d66ec33f83---4)*

### Décryptage pour l'Architecture Bancaire :

L'architecture présentée ci-dessus illustre la modernisation des traitements Data à grande échelle sur la plateforme **IBM watsonx.data**, un pattern particulièrement adapté aux exigences du secteur bancaire.

1. **Découplage API REST & Ingestion Asynchrone** : Contrairement aux approches legacy basées sur `spark-submit` en accès direct sur les nœuds de calcul, le point d'entrée s'effectue ici via une **API REST sécurisée par jeton IAM**. Cela permet d'orchestrer les batchs analytiques depuis nos ordonnanceurs d'entreprise (ex. Control-M ou Airflow) sans exposer l'infrastructure d'exécution.
2. **Architecture Lakehouse & Format Ouvert (Apache Iceberg)** : Les jobs PySpark effectuent la transformation et chargent les données structurées directement sur du **Cloud Object Storage (COS)** au format **Apache Iceberg**. Pour notre groupe, ce pattern offre une interopérabilité totale entre les moteurs analytiques (Presto, Spark, Db2) sans duplication physique des données, répondant directement à nos enjeux FinOps.
3. **Sécurité, Auditabilité & Traçabilité** : L'intégration native du contrôle d'accès IAM à chaque étape (soumission du job, accès au bucket de code Python, écriture dans la table cible) garantit une traçabilité conforme aux exigences réglementaires (BCBS 239 et RGPD), essentielle lors des audits de nos pipelines réglementaires.

---

## 🗺️ La Carte Stratégique (Wardley Map) de la Semaine

![Wardley Map - A good enough map](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEis7Jrf_1Hy_mo_wV3aRbkan8-1IbQI1YhzuyWJt4soGNWFQvA6tL1tV5QKk_-A0iRR1HcyEzpGqZkHGU0AGpn390Y5hR2DB20-nwrbNfEqrmrK5rrjLjdeofZfCzs6CHyrXVSaH8lFMT9UdSkLM7DfCbt2zDrIXqkLFadV4Xg6H4sTn-StJzlWKQ/w400-h281/graph.png)
*Source : [Simon Wardley (Gardeviance) — A good enough map](https://blog.gardeviance.org/2024/02/a-good-enough-map.html)*

### Analyse Stratégique d'Architecture :

L'application de la méthode de cartographie de Simon Wardley à nos infrastructures Cloud et d'IA met en évidence des mouvements industriels majeurs :

1. **Commoditisation des composants d'infrastructure et de calcul** : L'axe horizontal (de la *Genèse* vers la *Commodité*) confirme que le calcul d'inférence, le stockage d'objets et l'exécution de conteneurs sont aujourd'hui des utilités publiques (*Commodities*). Tenter de reconstruire des plateformes d'hébergement custom au lieu d'exploiter les services managés cloud (sur GCP, AWS ou IBM Cloud) génère une dette d'inertie organisationnelle dommageable.
2. **Glissement de la valeur vers la donnée métier et le contexte** : Alors que les modèles de langage de base (LLM) migrent rapidement vers la catégorie des produits/commodités standards (favorisés par l'essor des modèles *open-weight*), la véritable valeur différenciante de la banque remonte le long de la chaîne de valeur verticale. La valeur réside désormais dans nos **graphes de connaissances (GraphRAG)**, nos **référentiels sémantiques** et notre capacité à sécuriser le contexte applicatif.
3. **Inertie organisationnelle et réponse d'architecture** : La carte met en exergue l'inertie causée par les processus d'approbation traditionnels lorsqu'ils s'appliquent à des composants évoluant vers la commodité. La mise en place de **passerelles agnostiques (AI Gateways)** et l'adoption de **standards stateless (comme MCP)** constituent le levier stratégique pour libérer nos équipes de développement tout en maintenant la barrière de contrôle d'entreprise.

---

## 🚀 Projets Pilotes à Lancer sous 3 Mois

Pour transformer cette veille en valeur opérationnelle, voici 4 propositions de projets pilotes (*PoC / MVP*) directement alignés avec nos priorités stratégiques :

### Pilote 1 : Déploiement d'une Passerelle IA (AI Gateway) & MCP Stateless
* **Objectif** : Valider la capacité d'une passerelle centralisée à appliquer des règles de routage sémantique, de contrôle de coût et de sécurité sur des serveurs d'outils MCP stateless sans dégradation de latence (<15ms d'overhead).
* **Périmètre équipe (~10 personnes)** : 1 Architecte Solution, 2 Ingénieurs DevOps/Cloud, 3 Développeurs Backend (Go/Java), 2 Ingénieurs Sécurité, 1 Data Engineer, 1 Tech Lead.
* **Durée & Jalons** :
  * *M1* : Déploiement de l'AI Gateway sur environnement Sandbox et implémentation du protocole MCP Stateless pour 2 services internes.
  * *M2* : Intégration du routage dynamique (modèle interne open-weight vs API managée externe) et injection de garde-fous de sécurité.
  * *M3* : Benchmarking sous charge (1000 req/sec) et restitution des métriques FinOps.
* **Critères de succès** : 100% des requêtes auditées avec identité propre ; réduction de 25% des coûts de jetons par routage intelligent ; temps de réponse supplémentaire < 15ms.
* **Risques & Mitigation** : Latence sur le routage sémantique ➔ Utiliser des modèles d'ambassadeurs ultra-légers (ex. Small Language Models / MoE) au niveau du proxy edge.

### Pilote 2 : Framework d'Autonomie Graduée pour Agents de Support IT
* **Objectif** : Tester un modèle d'habilitation dynamique (*Graduated Autonomy*) où un agent IA effectue des remédiations sur le SI selon son score de confiance et le niveau de réversibilité des actions.
* **Périmètre équipe (~10 personnes)** : 1 Architecte Sécurité/IAM, 2 Développeurs Python/AI, 2 Ingénieurs SRE, 1 Tech Lead, 2 Experts Domaine IT Operations, 1 Product Owner, 1 UX Designer.
* **Durée & Jalons** :
  * *M1* : Modélisation des politiques d'accès Cedar/IAM et définition de la grille de réversibilité des actions IT.
  * *M2* : Développement de l'agent d'infrastructure connecté à Bedrock AgentCore / Azure Foundry et intégration de l'approbation humaine (*HITL*).
  * *M3* : Déploiement en production restreinte sur la gestion des réinitialisations de comptes et diagnostics d'incidents mineurs.
* **Critères de succès** : Zero action destructrice non autorisée exécutée ; réduction de 40% du temps moyen de résolution (MTTR) sur le périmètre pilote ; traçabilité d'audit à 100%.
* **Risques & Mitigation** : Risque d'escalade non contrôlée de privilèges ➔ Isolation stricte du processus de contrôle des politiques en dehors du temps d'exécution de l'agent (*out-of-process Policy Engine*).

### Pilote 3 : Rationalisation FinOps par Right-Sizing Automatisé des Conteneurs
* **Objectif** : Mettre en œuvre un mécanisme d'ajustement automatique des ressources CPU/Mémoire (*Container Right-Sizing*) inspiré du modèle Stratum de Netflix sur nos clusters Kubernetes (AKS/EKS).
* **Périmètre équipe (~9 personnes)** : 1 Architecte Cloud, 3 Ingénieurs FinOps/Platform, 2 Développeurs Kubernetes, 1 Expert Performance, 1 Tech Lead, 1 Product Owner.
* **Durée & Jalons** :
  * *M1* : Déploiement des sondes d'observabilité et collecte des métriques réelles de consommation sur un namespace applicatif non-critique.
  * *M2* : Implémentation de l'algorithme d'analyse des profils de charge et génération de recommandations automatisées de découpes de conteneurs.
  * *M3* : Activation du redimensionnement automatique en environnement de staging et pré-production.
* **Critères de succès** : Réduction d'au moins 20% des ressources mémoire et CPU réservées non utilisées ; aucun incident d'OOM (*Out Of Memory*) généré lors des tests de charge.
* **Risques & Mitigation** : Risque de sous-provisionnement sur pics de charge imprévus ➔ Fixation de seuils de sécurité (*buffers*) minimaux inviolables et intégration avec les métriques KEDA.

### Pilote 4 : Évaluation Continue des Dérives LLM via le Pattern "LLM-as-a-Judge"
* **Objectif** : Déployer un pipeline automatisé d'évaluation de la qualité des réponses génératives pour un cas d'usage bancaire (analyse de conformité réglementaire) avec boucle d'alignement humain.
* **Périmètre équipe (~10 personnes)** : 1 Architecte Data/AI, 3 Data Scientists / ML Engineers, 2 Développeurs Backend, 2 Experts Métier Conformité, 1 Data Governance Manager, 1 PO.
* **Durée & Jalons** :
  * *M1* : Constitution du jeu de données de référence ("Gold Dataset") avec l'équipe Conformité et choix du modèle évaluateur.
  * *M2* : Déploiement du pipeline d'évaluation automatisé et mise en place des métriques de fidélité, pertinence et sécurité.
  * *M3* : Simulation de dérives comportementales et validation de la capacité du système à alerter et bloquer les réponses non conformes.
* **Critères de succès** : Taux d'accord entre le LLM-Juge et l'évaluation humaine > 90% ; détection des hallucinations en moins de 2 secondes.
* **Risques & Mitigation** : Biais ou dérive du modèle juge lui-même ➔ Audit aveugle récurrent par échantillonnage aléatoire soumis aux experts métiers.

---

## 💬 Conclusion & Échange

La transition vers un SI piloté par les agents autonomes et rationalisé par le FinOps ne se fera pas en empilant des technologies, mais en repensant nos cadres de contrôle et nos architectures applicatives.

**Question pour nos débats d'architecture cette semaine :** 
*Face à l'explosion des coûts liés à la surcharge des fenêtres de contexte, devez-vous privilégier la restriction stricte du contexte envoyé à un modèle principal, ou investir massivement dans des architectures multi-agents distribuées malgré la "taxe d'orchestration" qu'elles induisent ?*

N'hésitez pas à faire part de vos retours en commentaire ou lors de nos prochains comités d'architecture.