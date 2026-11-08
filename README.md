# 🏛️ Veille Tech Agent — Système Multi-Agents de Veille Stratégique SI

Système multi-agents autonome de veille technologique et stratégique conçu pour les **Architectes d'Entreprise** (spécialisé Banque, Assurance, Énergie, Systèmes Distribués, IA Agentique, Agent Développeur & Développeur Augmenté).

---

## 🚀 Déploiement Rapide sur MacBook (macOS)

Ce projet est optimisé pour macOS (Apple Silicon M1/M2/M3/M4 & Intel).

### 1. Prérequis
* Un MacBook sous macOS (12 Monterey, 13 Ventura, 14 Sonoma, 15 Sequoia ou ultérieur).
* **Python 3.10+** (inclus par défaut avec Xcode CLI Tools `xcode-select --install` ou via Homebrew `brew install python`).
* Une clé API **Mistral AI** (disponible sur [Mistral Console](https://console.mistral.ai/api-keys/)) ou Google Gemini ([Google AI Studio](https://aistudio.google.com/app/apikey)).

### 2. Installation en 1 commande

Ouvrez le Terminal dans le dossier du projet et lancez :

```bash
./install.sh
```

Le script s'occupe de tout :
1. Détection de votre environnement Python macOS.
2. Création de l'environnement virtuel isolé (`./venv`).
3. Installation des dépendances requises (`requirements.txt`).
4. Création de l'arborescence de données (`data/raw`, `data/summaries`, `data/newsletters`).
5. Préparation du fichier `.env`.

---

## ⚙️ Configuration

### Clé API & Modèle LLM
Vous pouvez renseigner votre clé API soit :
* Directement dans le fichier `.env` :
  ```env
  MISTRAL_API_KEY="votre_cle_api_mistral"
  # GEMINI_API_KEY="votre_cle_api_gemini" # Alternative
  EMAIL_SENDER="votre.email@gmail.com"     # Optionnel
  ```
* Ou via l'assistant interactif qui permet de basculer facilement entre **Mistral AI**, **Google Gemini**, **Ollama (local)** ou **IBM WatsonX** :
  ```bash
  ./run.sh configure
  ```

### Sources de Veille
Les flux RSS et newsletters sont configurés dans `config/sources.yaml` :
* **Cloud & Infrastructure** : AWS Architecture, Microsoft Azure, Netflix TechBlog, Cloudflare, Uber Eng, Last Week in AWS, ByteByteGo, Off-by-none...
* **Ingénierie Logicielle & Modernisation** : Martin Fowler, Gregor Hohpe, Refactoring.fm, InfoQ, TLDR Tech...
* **Data, IA Agentique & Banques** : Capital One Tech, Neo4j, Claude Dev, Simon Wardley (Gardeviance), IBM Cloud & watsonx, Google Cloud Community...
* **Agent Développeur & Ingénierie Augmentée** : GitHub Copilot & AI Blog, Simon Willison, Cursor Blog, JetBrains AI, Qodo (CodiumAI), Sourcegraph Cody, Addy Osmani...

### 📰 Structure de la Newsletter Hebdomadaire
1. **Rationalisation & Simplification du SI**
2. **Architecture Évolutive & Ingénierie Logicielle**
3. **Data & Agentic AI**
4. **Agent Développeur & Développeur Augmenté** *(IDEs agentiques, copilotes d'ingénierie, agents SWE autonomes, tests & revues IA, DevEx, gouvernance et dette technique)*
5. **IA & Métiers Bancaires (Retail, Asset Management, CIB)** *(Scoring temps réel, agents conversationnels KYC/service client, synthèse financière et de sentiment, allocation assistée, analyse de contrats et structuration de deals, surveillance de marchés et post-trade)*
6. **Infographie Technique de la Semaine** *(Priorité IBM Cloud / Google Cloud Platform)*
7. **Carte Stratégique (Wardley Map)** *(Simon Wardley / Wardley Maps Community)*
8. **Projets Pilotes à Lancer sous 3 Mois** *(Feuilles de route opérationnelles et dimensionnées pour des équipes de ~10 personnes)*
9. **Projets Réels Passés à l'Échelle** *(Retours d'expérience documentés et chiffrés pour nos axes stratégiques et cas bancaires)*

---

## 💻 Utilisation Quotidienne

Des raccourcis simples sont fournis via `./run.sh` :

```bash
# 1. Collecte quotidienne et filtrage LLM des articles du jour
./run.sh daily

# 2. Rédaction de la newsletter hebdomadaire + génération de la page HTML multilingue (7 langues)
./run.sh weekly

# 3. Rédaction, page multilingue et envoi automatique par email
./run.sh weekly --send-email

# 4. Régénération à la demande de la page HTML multilingue (sans re-calcul LLM complet)
./run.sh html

# 5. Assistant de configuration interactive
./run.sh configure
```

Les newsletters générées sont sauvegardées automatiquement dans `data/newsletters/` :
* Format Markdown : `data/newsletters/newsletter_AAAA-MM-JJ.md`
* Versions traduites (7 langues) : `data/newsletters/newsletter_AAAA-MM-JJ_{fr,en,nl,pl,it,tr,uk}.md`
* Page web interactive multilingue : `data/newsletters/multilingual_newsletter.html` (avec sélecteur dynamique et auto-détection de la langue du navigateur).

---

## 🕒 Automatisation sur macOS (Crontab)

Pour que votre MacBook exécute la veille en arrière-plan :
* **Collecte quotidienne** : tous les matins à 06h00.
* **Génération hebdomadaire** : tous les dimanches soir à 19h00.

Lancez l'assistant automatique :
```bash
./setup_cron.sh
```

*(Ou configurez manuellement votre crontab via `crontab -e`)*.

---

## 📂 Structure du Projet

```text
veille_tech_agent/
├── agents/                  # Multi-agents Python
│   ├── collector.py         # Collecte RSS & extraction d'images/infographies
│   ├── evaluator.py         # Scoring & résumés structurés par IA (score >= 7/10)
│   ├── writer.py            # Synthèse hebdomadaire, Wardley Map & projets pilotes
│   ├── mailer.py            # Envoi SMTP sécurisé en HTML/Markdown
│   └── llm_client.py        # Client unifié (Gemini / WatsonX / Ollama)
├── config/
│   ├── sources.yaml         # Liste des flux RSS et médias surveillés
│   ├── email_config.yaml    # Paramètres SMTP et destinataires
│   └── llm_config.yaml      # Paramètres du modèle LLM
├── data/
│   ├── raw/                 # Articles bruts ingérés (JSON)
│   ├── summaries/           # Résumés évalués (JSON)
│   └── newsletters/         # Newsletters finales publiées (Markdown)
├── install.sh               # Script d'installation automatique macOS
├── run.sh                   # Lanceur rapide en CLI
├── setup_cron.sh            # Assistant d'automatisation crontab
├── cron_daily.sh            # Script cron quotidien
├── cron_weekly.sh           # Script cron hebdomadaire
├── configure.py             # Assistant interactif de configuration
├── requirements.txt         # Dépendances Python
├── .env.example             # Modèle de variables d'environnement
└── README.md                # Documentation complète
```
