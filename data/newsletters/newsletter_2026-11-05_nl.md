# Technologische Verkenning #124: Het Tijdperk van Agentische Architectuur en Geaugmenteerde Ontwikkeling

Deze week bevestigt onze technologische verkenning een fundamentele verschuiving in software-engineering en enterprise-architectuur: we transformeren van experimentele chatinterfaces naar **industriële agentische engineering**. De nadruk ligt niet langer uitsluitend op het genereren van code, maar op enterprise-governance, kostenefficiëntie per eenheid (FinOps) en het beheersen van afhankelijkheidsketens binnen complexe gedistribueerde systemen.

---

## 1. 🔄 Rationalisatie & Vereenvoudiging van het Informatiesysteem
De belangrijkste les uit de recente engineeringervaringen bij Netflix en Cloudflare is eenduidig: prestaties zijn een directe functie van eenvoud. Cloudflare bespaarde meer dan 100 TB aan RAM dankzij algoritmische optimalisaties (consistent hashing geïmplementeerd in Rust), terwijl Netflix zijn Apache Flink autoscaling-componenten herijkt om te standaardiseren op open-source standaarden. Voor een grote bankgroep onderstreept dit de noodzaak om wildgroei aan interne componenten te stoppen ("bouwen versus adopteren") en te focussen op robuuste, gestandaardiseerde fundamenten.

*   [Geheugenoptimalisatie bij Cloudflare](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)
*   [Autoscaling van Apache Flink bij Netflix](https://netflixtechblog.com/a-tale-of-two-flink-autoscalers-e9f6a1b1492b)

## 2. 🏗️ Evolutionaire Architectuur & Software Engineering
De opkomst van **AI Gateways** en het **Model Context Protocol (MCP)** vormt een structureel speerpunt voor onze enterprise-architectuur. Deze ontwerppatronen ontkoppelen AI-modellen van operationele applicaties en creëren één centraal controlepunt voor auditering, compliance, telemetrie en beleidshandhaving. Daarnaast vormt de overstap naar *stateless* architecturen binnen het MCP-protocol een cruciale stap voor serverless implementaties (AWS Lambda, Bedrock), waardoor horizontale schaalbaarheid mogelijk wordt zonder complexe sessiebeheersing.

*   [Evolutionaire Architectuur en AI Gateways](https://www.infoq.com/articles/evolutionary-architecture-pattern/)
*   [MCP en Stateless Architectuur voor Serverless](https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/)

## 3. 🧠 Data & Agentic AI
Data blijft de brandstof, maar de structuur ervan wordt nu gedicteerd door de vereisten van autonome agenten. Praktijkresultaten rondom **GraphRAG** (het koppelen van graafdatabases zoals Amazon Neptune aan LLM's) tonen een drastische reductie (tot 90%) in enterprise-modelleerinspanningen. Door LLM's te verankeren in rigoureuze bedrijfskundige ontologieën elimineren we hallucinaties en borgen we de strikte wettelijke conformiteit die vereist is voor onze KYC- en AML-processen.

*   [MUFG Bank: 90% Tijdswinst bij Procesmodellering](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)
*   [Contextuele Ophaalstrategieën en GraphRAG](https://neo4j.com/blog/agentic-ai/contextual-retrieval/)

## 4. 💻 Developer Agent & Geaugmenteerde Ontwikkelaar (Augmented Developer)
We betreden definitief het tijdperk van **geaugmenteerde software-engineering**. Agenten fungeren niet langer slechts als invoerhulp, maar als volwaardige workflow-orchestrators (bijv. Claude Code, Qodo).

*   **De Productiviteitsparadox**: Tools zoals GitHub Copilot (via de speciale Java SDK) en agentische IDE's zoals Cursor veranderen de dynamiek van softwareontwikkeling. Het operationele knelpunt is verschoven van coderen naar codereviews, architecturale validatie en kwaliteitsborging.
*   **Governance en Veiligheid**: Geautomatiseerde reviews en testgeneratie door agenten (zoals Google Mantis en Qodo) zijn inmiddels onmisbare standaarden. We moeten echter waakzaam blijven voor *Skill Decay* (het verlies van technische vaardigheden): de menselijke architect en ontwikkelaar moeten aan het stuur blijven om structurele architectuurkeuzes te valideren.
*   **Infrastructuur**: GitHub en Anthropic herdefiniëren versiebeheer om autonome agenten te ondersteunen die continu commits uitvoeren zonder codebases te blokkeren.

*   [GitHub Copilot SDK voor Java](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)
*   [Governance van Developer Agents met JetBrains Air Governance](https://blog.jetbrains.com/ai/2026/11/livestream-scaling-agentic-development-with-air-governance/)

---

## 📊 Technische Infographic van de Week

![Validatie van AI-modellen via deterministische tests (Google Cloud / Vertex AI)](https://cdn-images-1.medium.com/max/1024/1*L-sfIHDoKW1COd8Dyq7Pkg.png)

*Bron: [Google Cloud Community - A New Model Is Not an Upgrade Until Your Evals Say So](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e)*

**Architecturale Analyse**: Dit schema illustreert het doorslaggevende belang van deterministische testsuites (gebaseerd op Pydantic-schema's en strenge conformiteitstests) bij de introductie van nieuwe modelversies. Vóór de afdwinging van strikte schemacontracten was de aansluiting op bedrijfsregels wisselvallig. Na implementatie nam de operationele betrouwbaarheid exponentieel toe.
**Operationele Aanbeveling**: Breng een agent nooit in productie zonder structurele validatietesten en canarietests. In de financiële sector vormt een agent die een transactieformaat hallucineert een onaanvaardbaar operationeel risico.

---

## 🗺️ Strategische Kaart (Wardley Map) van de Week

![Wardley Map - Evolutie van de Applicatie-ontwikkelstack & Serverless](https://cdn-images-1.medium.com/max/1024/1*-oZD4wPJkqOPQbuLPSCF0Q.jpeg)

*Bron: [Simon Wardley — On playing chess (Wardley Maps Publication)](https://medium.com/wardleymaps/on-playing-chess-2634b825dbac)*

**Strategische Analyse**: Deze kaart toont de structurele verschuiving van het zwaartepunt in software-engineering: door compute en applicatieruntimes naar volwaardige nutsvoorzieningen (*Commodity/Utility* via Serverless en managed platforms) te duwen, verdwijnt operationele infrastructuur naar de achtergrond. Tijd die voorheen verloren ging aan *Yak Shaving* (serverconfiguratie, OS-patching, capaciteitsplanning) komt volledig vrij voor directe bedrijfswaarde.
**Strategische Zet**: Met de opkomst van autonome programmeeragenten verschuift zelfs codegeneratie naar industriële standaardisatie. De strategische meerwaarde van de architect en software-engineer verplaatst zich definitief naar de top van de waardeketen: multi-agent orkestratie, contextuele beveiliging en overkoepelende enterprise-architectuur.

---

## 🚀 Proefprojecten om binnen 3 Maanden te Lanceren

1.  **Pilootproject Beheerde Developer Agent**:
    *   **Doel**: Valideren van het gecontroleerde gebruik van een agentische IDE (type Cursor/Continue) op een legacy codebase met *Air Governance* ter bewaking van tokenniveau en kosten.
    *   **Omvang**: 1 team van ~10 engineers.
    *   **Mijlpalen**: M1 (Installatie & Beveiligingsrichtlijnen), M2 (Gerichte onderhoudstaken), M3 (Meting productiviteit & kwaliteit).
    *   **Succescriteria**: 20% kortere doorlooptijd bij foutoplossing, strikte naleving van tokenlimieten.

2.  **Pilootproject GraphRAG voor Compliance**:
    *   **Doel**: Automatiseren van de identificatie van UBO's (Uiteindelijk Belanghebbenden) uit ongestructureerde KYC-dossiers met behulp van Amazon Neptune en Bedrock.
    *   **Omvang**: 1 Data Engineer, 1 Data Scientist, 1 Compliance-expert.
    *   **Succescriteria**: Nauwkeurigheid > 95% vergeleken met handmatige audits.

3.  **Pilootproject Enterprise AI Gateway**:
    *   **Doel**: Centraliseren van alle interne LLM-aanroepen via één gateway voor kostenmonitoring, contentinspectie en semantische routering.
    *   **Omvang**: 1 Solution Architect, 2 Platform/SRE Engineers.
    *   **Succescriteria**: 100% inzichtelijkheid in API-verkeer, extra routeringsvertraging < 15ms.

---

## 🏢 Reële Projecten op Schaal (Publieke Casestudies)

1.  **MUFG Bank (Rationalisatie)**:
    *   **Project**: Op ontologie gebaseerde AI voor de standaardisatie van wereldwijde bedrijfsprocessen en stroomdiagrammen (Amazon Neptune & Bedrock).
    *   **Resultaat**: **90% reductie** in documentatiedoorlooptijden (teruggebracht van 11 werkdagen naar slechts 1 dag). [Referentie: AWS Database Blog](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

2.  **Netflix (Evolutionaire Architectuur)**:
    *   **Project**: Stratum Resource Tuner (Geautomatiseerde container-rightsizing op schaal).
    *   **Resultaat**: Geautomatiseerde en continue optimalisatie van CPU- en geheugentoewijzingen, waardoor overprovisioning en cloudkosten drastisch worden ingeperkt. [Referentie: Netflix Tech Blog](https://netflixtechblog.medium.com/netflix-stratum-media-processing-automated-container-right-sizing-ddf9aa68a801)

3.  **Capital One (Data & Agentic AI)**:
    *   **Project**: Implementatie van multi-agentsystemen voor deterministisch en betrouwbaar redeneren over broncode (*FinRT*).
    *   **Resultaat**: Industriële verankering van geautomatiseerde beveiligingsscans en kwetsbaarheidsdetectie binnen de bancaire ontwikkelcyclus. [Referentie: Capital One Tech](https://medium.com/capital-one-tech/advancing-safe-agentic-ai-asks-symposium-highlights-bbba40b19784)

4.  **Dynata (Geaugmenteerde Ontwikkelaar)**:
    *   **Project**: Brede adoptie van de AI-DLC-methodologie in combinatie met de Kiro IDE.
    *   **Resultaat**: Oplevering van complexe features binnen **1 sprint in plaats van 4**, dankzij naadloze contextuele integratie tussen projectdocumentatie (Jira/Confluence) en codebases. [Referentie: AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/)

---

*De centrale vraag voor onze teams deze week: Zijn we er organisatorisch klaar voor om te accepteren dat onze primaire meerwaarde morgen niet meer ligt in het intypen van code, maar in het orkestreren, valideren en besturen van de agenten die deze code schrijven en controleren?*
