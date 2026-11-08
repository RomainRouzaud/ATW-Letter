# ⚡ Le Brief de l'Archi : Gérer l'explosion du code IA, souveraineté des LLM et résilience opérationnelle

Bonjour à tous,

En tant qu'architectes au sein d'un grand groupe bancaire européen, nous faisons face à un double défi cette semaine. D'un côté, l'entrée en vigueur imminente de la réglementation **DORA** nous impose une résilience opérationnelle et une maîtrise absolue de nos flux. De l'autre, la déferlante de l'IA générative bouscule notre modèle d'ingénierie et de gouvernance. 

Cette semaine, ma veille se concentre sur les dynamiques de l'IA en production, la crise de croissance que subissent nos cycles de livraison de code, et les nouvelles approches d'infrastructure pour garantir notre souveraineté et notre résilience.

Bonne lecture !

---

## 🏛️ L'Industrialisation de l'IA Générative : Souveraineté, Passerelles et Coûts d'Orchestration

L'heure n'est plus aux POCs (Proof of Concepts) sur des API tierces. Pour un grand groupe financier, les enjeux de souveraineté des données, de conformité réglementaire et de maîtrise des coûts imposent une transition vers des architectures maîtrisées de bout en bout.

### 1. L'hébergement souverain à l'échelle
Le retour d'expérience de Netflix sur l'hébergement interne de ses LLM ([In-House LLM Serving at Netflix](https://netflixtechblog.com/in-house-llm-serving-at-netflix-a5a8e799ea2c?source=rss----2615bd06b42e---4)) est une mine d'or. En s'appuyant sur l'architecture vLLM et Triton Inference Server, ils démontrent qu'il est possible de découpler finement les artefacts des modèles de l'infrastructure de service. Pour nos banques, c'est la preuve qu'héberger nos propres modèles (ouverts ou spécialisés) sur nos cloud privés ou environnements hybrides n'est pas seulement une exigence de sécurité, c'est une option techniquement et économiquement viable.

### 2. Le pattern de l'AI Gateway pour stabiliser l'architecture
Face à la volatilité des modèles et des API d'IA, InfoQ propose un pattern d'architecture évolutif indispensable : l'**AI Gateway** ([An Evolutionary Architecture Pattern for Managing AI’s Pace of Change](https://www.infoq.com/articles/evolutionary-architecture-pattern/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Architecture)). Ce composant agit comme une couche d'abstraction et de découplage. Il centralise les garde-fous (guardrails) de sécurité, le routage sémantique, l'auditabilité des requêtes et la gestion d'identité des agents sans impacter les applications métiers.

### 3. La taxe d'orchestration et le "Human-in-the-Loop"
Lorsque nous concevons des systèmes d'agents complexes, Martin Fowler introduit un concept clé : "The Orchestrator's Tax" ([The Orchestrator's Tax](https://martinfowler.com/articles/orchestrator-tax.html)). L'utilisation de sous-agents ne sert pas uniquement à paralléliser les tâches, mais surtout à protéger la fenêtre de contexte (*context window*) de l'orchestrateur principal. Une mauvaise délégation surcharge le modèle central, dégrade la pertinence et fait exploser les coûts de transaction (tokens). 

Pour intégrer ces agents dans nos processus réglementés, l'architecture événementielle et serverless proposée par AWS ([Building a serverless AI assistant at Pelago](https://aws.amazon.com/blogs/architecture/building-a-serverless-ai-assistant-at-pelago-concept-to-care-in-two-weeks/)) montre comment imbriquer un contrôle humain obligatoire (*Human-in-the-Loop*) de manière asynchrone, garantissant la conformité sans bloquer l'expérience utilisateur.

---

## 💻 Le Paradoxe de la Productivité : Surcharge de Code et Crise des Revues

Si l'IA générative promet de démultiplier la productivité de nos développeurs, elle déplace les goulots d'étranglement de manière critique au sein de notre cycle de vie logiciel (SDLC).

```
[Avant IA]  Développement (Lent) ──> Revue de Code (Rapide) ──> Déploiement
[Avec IA]   Développement (Ultra-Rapide) ──> REVUE DE CODE (GOULOT D'ÉTRANGLEMENT) ──> Déploiement
```

### 1. Le coût réel du "Oui" a changé
Comme le souligne très bien l'ingénierie de GitHub ([The cost of saying yes has changed](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/)), générer la première version d'un code ne coûte plus rien. Le véritable coût réside désormais dans la maintenance à long terme, la conformité, la sécurité et la dette technique (le *Total Cost of Ownership*). La gouvernance du scope projet doit évoluer : au lieu de débattre de la faisabilité technique, nous devons arbitrer sur la responsabilité et la capacité de l'humain à maintenir ce code généré.

### 2. Le goulot d'étranglement des Pull Requests
Gergely Orosz tire la sonnette d'alarme ([The Pulse: concern about massive increase in code review load](https://blog.pragmaticengineer.com/the-pulse-new-trend-concern-about-massive-increase-in-code-review-load/)) : l'adoption massive des assistants de code provoque une explosion du volume de code à relire. Les développeurs seniors passent leurs journées à réviser des PRs massives, risquant la fatigue cognitive et l'approbation aveugle (*rubber-stamping*). Des entreprises comme Uber ou Cloudflare déploient activement des outils d'IA pour pré-analyser le risque des PRs.

Toutefois, attention à l'effet pervers des mauvais outils d'IA. GitHub partage ses apprentissages sur l'amélioration de son propre agent de revue de code ([Better tools made Copilot code review worse](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/)). En fournissant trop de contexte à l'agent (recherche large dans tout le repo), l'outil s'est dégradé en entrant dans des boucles d'analyse infinies (*browsing loops*). C'est en recentrant l'IA sur le comportement ciblé d'un réviseur humain (analyse stricte du *diff*) qu'ils ont réduit les coûts de 20 % tout en améliorant considérablement la pertinence des remarques.

### 3. La modernisation des architectures legacy
L'IA n'est pas qu'une usine à nouvelles fonctionnalités, c'est aussi un levier de modernisation. L'étude de cas sur la réécriture du runtime Bun de Zig vers Rust ([The Pulse: What can we learn from Bun’s rapid Rust rewrite with AI?](https://blog.pragmaticengineer.com/the-pulse-what-can-we-learn-from-buns-rapid-rust-rewrite-with-ai/)) démontre que l'IA change radicalement l'équation économique des réécritures complètes de systèmes complexes, permettant d'adopter des langages garantissant la sécurité mémoire (*memory safety*) à un coût jusqu'ici prohibitif.

---

## 🛡️ Résilience Active et Sécurité des Infrastructures Modernes

En tant qu'institution financière, la robustesse de nos fondations reste notre priorité non négociable.

*   **Observabilité et topologies dynamiques :** Netflix détaille comment ils cartographient leurs dépendances de services à grande échelle en temps réel en combinant des flux **eBPF** et Kafka ([Building Service Topology at Scale](https://netflixtechblog.com/building-service-topology-at-scale-architecture-challenges-and-lessons-learned-f4b792f3f0d8?source=rss----2615bd06b42e---4)). Leur principal enseignement réside dans la gestion de la contre-pression réactive (*reactive backpressure*) pour éviter l'effondrement des systèmes d'observabilité lors d'incidents majeurs.
*   **Privacy par Design (Zero Trust) :** Cloudflare libère en open-source `pvcli` ([We’re open-sourcing our privacy proxy CLI](https://blog.cloudflare.com/open-sourcing-our-privacy-proxy-cli/)), un outil facilitant l'adoption d'**Oblivious HTTP (OHTTP)**. Ce protocole permet de dissocier l'identité de l'utilisateur (IP) de la requête applicative grâce à un relais tiers de confiance. Une technologie d'avenir pour nos architectures de transactions anonymisées ou de télémétrie hautement confidentielle.
*   **Résilience Multi-Régions :** AWS propose un guide rigoureux sur la haute disponibilité active-active de nos déploiements d'infrastructures ([Building multi-Region resiliency for AWS CloudFormation custom resource deployment](https://aws.amazon.com/blogs/architecture/building-multi-Region-resiliency-for-AWS-CloudFormation-custom-resource-deployment/)). En utilisant des verrous distribués via DynamoDB Global Tables, ils sécurisent les déploiements d'infrastructures multi-régions sans risque d'exécutions concurrentes destructrices.

---

## 🚀 Projets Pilotes à Lancer sous 3 Mois

Pour transformer ces insights en valeur concrète pour notre groupe bancaire, voici 4 propositions de projets pilotes applicables rapidement :

### Pilote 1 : L'AI Gateway d'Entreprise Souveraine
*   **Objectif :** Valider la capacité à centraliser, auditer et sécuriser la consommation des LLM (externes et internes) via une passerelle unique sans ajouter de latence critique (> 50ms).
*   **Périmètre équipe (~10 personnes) :** 1 Architecte d'Entreprise, 1 Expert SecOps, 2 Ingénieurs DevOps, 3 Développeurs Backend (Go/Java), 1 Data Engineer, 1 Product Owner, 1 QA.
*   **Durée & Jalons :**
    *   *Mois 1 :* Choix technique (ex: APISIX ou Kong) et mise en place du routage sémantique de base vers nos modèles internes (vLLM) et cloud (Azure OpenAI).
    *   *Mois 2 :* Implémentation des mécanismes de masquage de données sensibles (PII/données bancaires) et de l'audit trail dans la passerelle.
    *   *Mois 3 :* Intégration sur 2 applications pilotes et tests de charge avec mesures de latence et d'efficacité des filtres de sécurité.
*   **Critères de succès :** 100 % des fuites de données d'identification (PII) bloquées en amont ; Latence additionnelle induite par la Gateway < 40ms.
*   **Risques :** Surcharge de latence liée au traitement sémantique. *Mitigation :* Mettre en œuvre des modèles de filtrage ultra-légers en local sur la passerelle pour les scans de sécurité rapides.

### Pilote 2 : "AI-Assisted Code Guard" - Automatisation des Revues
*   **Objectif :** Désengorger les revues de code de nos équipes en intégrant un agent d'IA focalisé exclusivement sur la conformité aux standards de sécurité bancaires et le respect du Clean Code sur le *diff*.
*   **Périmètre équipe (~10 personnes) :** 1 Lead Developer, 1 Architecte Logiciel, 4 Développeurs Senior, 1 Ingénieur AppSec (Sécurité Applicative), 1 Ingénieur DevOps (CI/CD), 1 PO, 1 QA.
*   **Durée & Jalons :**
    *   *Mois 1 :* Définition des règles de codage critiques (OWASP Top 10, patterns d'architecture internes) et configuration de l'agent IA (ex: invite système ciblée sur le diff).
    *   *Mois 2 :* Intégration de l'agent dans notre plateforme Git (GitLab CI / GitHub Actions) pour commenter automatiquement les Pull Requests.
    *   *Mois 3 :* Déploiement auprès de 3 équipes pilotes et ajustement des invites pour réduire le bruit (faux positifs).
*   **Critères de succès :** Temps moyen de validation des PR réduit de 30 % ; Taux de pertinence des commentaires de l'IA > 80 % (évalué par les développeurs).
*   **Risques :** Rejet de l'outil par les développeurs face à des faux positifs répétés. *Mitigation :* Brider l'agent à un périmètre strict de règles factuelles (ex: détection de secrets, absence de tests unitaires sur les nouvelles fonctions, failles d'injection SQL) au démarrage.

### Pilote 3 : Cartographie Dynamique Zero-Trust via eBPF
*   **Objectif :** Obtenir une visibilité en temps réel de nos topologies de microservices et identifier instantanément les flux non autorisés ou anormaux sans modifier le code applicatif.
*   **Périmètre équipe (~10 personnes) :** 1 Architecte Infrastructure/Réseau, 3 Ingénieurs Plateforme/Kubernetes, 2 Spécialistes SecOps, 2 SRE (Site Reliability Engineers), 1 Développeur Backend, 1 PO.
*   **Durée & Jalons :**
    *   *Mois 1 :* Déploiement d'agents eBPF (ex: Cilium / Hubble) sur un cluster Kubernetes de non-production.
    *   *Mois 2 :* Collecte et agrégation des flux réseau, création de la topologie dynamique dans notre outil de monitoring.
    *   *Mois 3 :* Simulation d'incidents réseau (latence, saturation) et validation de la mise en place automatique des règles de contre-pression (*backpressure*).
*   **Critères de succès :** Détection automatique de 100 % des communications inter-services ; Surcharge CPU sur les nœuds applicatifs inférieure à 1.5 %.
*   **Risques :** Résistance des équipes de sécurité réseau face à l'installation d'outils bas niveau au niveau du noyau (kernel). *Mitigation :* Présenter les garanties d'eBPF en lecture seule dans un premier temps et impliquer les équipes de sécurité dès la phase de cadrage.

### Pilote 4 : Modernisation d'un Microservice Legacy vers une Version Sécurisée (Rust/Java Moderne)
*   **Objectif :** Évaluer l'accélération fournie par l'IA pour migrer un composant critique legacy (ex: C++ ou vieux Java) vers un langage moderne garantissant de meilleures performances et une sécurité mémoire accrue.
*   **Périmètre équipe (~10 personnes) :** 1 Architecte applicatif, 4 Développeurs (compétences Legacy + Cible), 2 Ingénieurs QA (automatisation des tests), 1 DevOps, 1 Expert Sécurité, 1 PO.
*   **Durée & Jalons :**
    *   *Mois 1 :* Choix et isolation du composant métier cible. Établissement d'un harnais de tests automatisés complet pour garantir le non-régression (approche boîte noire).
    *   *Mois 2 :* Utilisation assistée par IA (ex: Claude / Copilot) pour transcrire et réécrire la logique métier dans le langage cible (ex: Rust ou Java 21).
    *   *Mois 3 :* Phase de tests différentiels intensifs, benchmark de performance et déploiement en mode "Shadow" (double exécution en production sans impact).
*   **Critères de succès :** Couverture de tests de non-régression à 100 % ; Réduction des besoins en ressources CPU/Mémoire d'au moins 40 % ; Temps de migration réduit de moitié par rapport à une estimation manuelle.
*   **Risques :** L'IA réplique ou introduit des bugs logiques subtils indétectables par simple compilation. *Mitigation :* S'appuyer impérativement sur des tests de bout en bout (Input/Output matching) exécutés en parallèle sur l'ancien et le nouveau système.

---

## 💬 Débattons !

L'accélération de la production de code par l'IA nous force à repenser nos critères d'acceptabilité. **Le goulot d'étranglement de nos organisations n'est plus la capacité à écrire du code, mais notre capacité à le valider, le sécuriser et le maintenir.**

*Comment votre organisation fait-elle face à l'augmentation du volume de Pull Requests générées par IA ? Avez-vous déjà initié des démarches de revue assistée par IA ou de déploiement d'AI Gateways ?*

Partagez vos retours d'expérience en commentaire !