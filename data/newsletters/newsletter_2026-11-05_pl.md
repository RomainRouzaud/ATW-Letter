# Przegląd Technologiczny #124: Era Architektury Agentowej i Inżynierii Wspomaganej

W tym tygodniu nasz przegląd technologiczny potwierdza zasadniczy przełom w praktykach inżynierii oprogramowania i architektury korporacyjnej: przechodzimy od fazy eksperymentów opartych na prostych czatach do **przemysłowej inżynierii agentowej**. Punkt ciężkości przesuwa się z samego generowania kodu ku ładzie korporacyjnemu (governance), jednostkowej efektywności kosztowej (FinOps) oraz opanowaniu łańcuchów zależności w złożonych systemach rozproszonych.

---

## 1. 🔄 Racjonalizacja i Uproszczenie Systemu Informatycznego
Główny wniosek płynący z doświadczeń Netflixa i Cloudflare jest jednoznaczny: wysoka wydajność to pochodna prostoty. Cloudflare zaoszczędził ponad 100 TB pamięci RAM dzięki niskopoziomowym optymalizacjom algorytmicznym (consistent hashing zaimplementowany w języku Rust), podczas gdy Netflix rekonfiguruje swoje mechanizmy autoskalowania Apache Flink, standaryzując je w oparciu o otwarte oprogramowanie społecznościowe. Dla wiodącej grupy bankowej oznacza to konieczność zahamowania proliferacji wewnętrznych komponentów ("build vs. adopt") i skoncentrowania się na solidnych, ujednoliconych fundamentach.

*   [Optymalizacja pamięci w Cloudflare](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)
*   [Autoskalowanie Apache Flink w Netflixie](https://netflixtechblog.com/a-tale-of-two-flink-autoscalers-e9f6a1b1492b)

## 2. 🏗️ Architektura Ewolucyjna i Inżynieria Oprogramowania
Pojawienie się **AI Gateways** oraz standardu **Model Context Protocol (MCP)** stanowi kluczowy temat dla naszej architektury korporacyjnej. Wzorce te pozwalają na separację modeli AI od aplikacji biznesowych, tworząc centralny punkt kontroli dla audytu, zgodności regulacyjnej, telemetrii i bezpieczeństwa. Ponadto ewolucja standardu MCP w kierunku architektur *stateless* (bezstanowych) otwiera nowe możliwości dla wdrożeń serverless (AWS Lambda, Bedrock), umożliwiając horyzontalną skalowalność bez konieczności utrzymywania złożonego stanu sesji.

*   [AI Gateway i Wzorce Architektury Ewolucyjnej](https://www.infoq.com/articles/evolutionary-architecture-pattern/)
*   [Protokół MCP w Architekturze Bezstanowej](https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/)

## 3. 🧠 Data & Agentic AI
Dane pozostają głównym paliwem, jednak ich topologia jest obecnie bezpośrednio dyktowana wymogami autonomicznych agentów. Doświadczenia z wdrożeń **GraphRAG** (połączenie grafowych baz danych, takich jak Amazon Neptune, z modelami LLM) wykazują radykalną redukcję (nawet o 90%) nakładów pracy związanych z modelowaniem procesów biznesowych. Zakotwiczenie modeli językowych w ścisłych ontologiach eliminuje zjawisko halucynacji i zapewnia bezwzględną zgodność z normami prawnymi w procesach KYC i AML.

*   [MUFG Bank: 90% Oszczędności Czasu w Modelowaniu Procesów](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)
*   [Wyszukiwanie Kontekstowe i GraphRAG](https://neo4j.com/blog/agentic-ai/contextual-retrieval/)

## 4. 💻 Agent Programistyczny i Programista Wspomagany (Augmented Developer)
Wkraczamy w erę **inżynierii oprogramowania wspomaganej przez sztuczną inteligencję**. Agenci przestają być jedynie narzędziami autouzupełniania składni, stając się pełnoprawnymi orkiestratorami procesów wytwórczych (np. Claude Code, Qodo).

*   **Paradoks Produktywności**: Narzędzia pokroju GitHub Copilot (wykorzystujące dedykowany SDK dla Javy) oraz agentowe środowiska IDE (jak Cursor) diametralnie modyfikują charakter pracy inżynierskiej. Wąskim gardłem wytwarzania oprogramowania staje się przegląd kodu (code review), weryfikacja architektury oraz zarządzanie regresją.
*   **Ład i Bezpieczeństwo**: Automatyzacja przeglądów i generowania testów przez agentów (np. Google Mantis, Qodo) jest już standardem operacyjnym. Należy jednak monitorować ryzyko *Skill Decay* (erozji kompetencji technicznych): człowiek musi pozostać decydentem walidującym spójność struktur architektonicznych.
*   **Infrastruktura Wytwórcza**: GitHub i Anthropic redefiniują semantykę systemów kontroli wersji, aby umożliwić bezkolizyjne zatwierdzanie zmian przez agentów kodujących w trybie ciągłym.

*   [GitHub Copilot SDK dla języka Java](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)
*   [Zarządzanie Agentami Programistycznymi z JetBrains Air Governance](https://blog.jetbrains.com/ai/2026/11/livestream-scaling-agentic-development-with-air-governance/)

---

## 📊 Techniczna Infografika Tygodnia

![Walidacja modeli AI poprzez testy deterministyczne (Google Cloud / Vertex AI)](https://cdn-images-1.medium.com/max/1024/1*L-sfIHDoKW1COd8Dyq7Pkg.png)

*Źródło: [Google Cloud Community - A New Model Is Not an Upgrade Until Your Evals Say So](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e)*

**Analiza Architektoniczna**: Schemat ten obrazuje krytyczne znaczenie deterministycznych zestawów testowych (opartych na ścisłych schematach Pydantic i bramkach weryfikacji strukturalnej) podczas wprowadzania nowych wag modeli. Przed wprowadzeniem rygorystycznych kontraktów walidacja reguł biznesowych była niestabilna; po ich wdrożeniu niezawodność rozwiązania wzrosła skokowo.
**Wniosek Operacyjny**: Nigdy nie wdrażaj autonomicznego agenta na produkcję bez zestawu testów strukturalnych i wdrożeń kanarkowych. W instytucji finansowej agent generujący niepoprawny format transakcji stanowi krytyczne ryzyko operacyjne.

---

## 🗺️ Mapa Strategiczna (Wardley Map) Tygodnia

![Wardley Map - Ewolucja Stosu Aplikacyjnego i Serverless](https://cdn-images-1.medium.com/max/1024/1*-oZD4wPJkqOPQbuLPSCF0Q.jpeg)

*Źródło: [Simon Wardley — On playing chess (Wardley Maps Publication)](https://medium.com/wardleymaps/on-playing-chess-2634b825dbac)*

**Analiza Strategiczna**: Mapa ta ilustruje fundamentalne przesunięcie środka ciężkości inżynierii oprogramowania: przesunięcie mocy obliczeniowych i środowisk uruchomieniowych w stronę powszechnych mediów (*Commodity/Utility* poprzez Serverless i platformy zarządzane) sprawia, że infrastruktura staje się przezroczysta dla programistów. Czas marnowany dotychczas na *Yak Shaving* (konfigurację serwerów, łatkowanie OS, planowanie pojemności) zostaje w całości uwolniony na rzecz logiki biznesowej.
**Ruch Strategiczny**: Wraz z ekspansją agentów programistycznych samo pisanie kodu zaczyna dryfować w stronę przemysłowego towaru. Kluczowa wartość dodana inżyniera przesuwa się na sam szczyt łańcucha wartości: orkiestrację przepływów agentów, bezpieczeństwo kontekstu i spójność architektury korporacyjnej.

---

## 🚀 Projekty Pilotażowe do Uruchomienia w Ciągu 3 Miesięcy

1.  **Pilotaż: Zarządzany Agent Programistyczny**:
    *   **Cel**: Zweryfikowanie bezpiecznego wdrożenia agentowego IDE (Cursor/Continue) w repozytorium legacy przy użyciu *Air Governance* do kontroli kosztów i zużycia tokenów.
    *   **Zakres**: 1 zespół inżynieryjny (~10 osób).
    *   **Kamienie Milowe**: M1 (Instalacja i reguły bezpieczeństwa), M2 (Ukierunkowane zadania refaktoryzacji), M3 (Pomiary produktywności i długu technicznego).
    *   **Kryteria Sukcesu**: Skrócenie czasu debugowania o 20%, pełna zgodność z budżetem tokenów.

2.  **Pilotaż: GraphRAG dla Zgodności Regulacyjnej (Compliance)**:
    *   **Cel**: Automatyzacja identyfikacji ostatecznych beneficjentów rzeczywistych (UBO) w nieustrukturyzowanych dokumentach KYC przy użyciu Amazon Neptune i Amazon Bedrock.
    *   **Zakres**: 1 Data Engineer, 1 Data Scientist, 1 Oficer Compliance.
    *   **Kryteria Sukcesu**: Precyzja i kompletność > 95% w odniesieniu do weryfikacji manualnej.

3.  **Pilotaż: Korporacyjna Brama AI (AI Gateway)**:
    *   **Cel**: Centralizacja wszystkich wewnętrznych wywołań LLM przez bramę pośredniczącą w celu monitorowania kosztów, filtrowania zapytań i routingu semantycznego.
    *   **Zakres**: 1 Architekt Rozwiązania, 2 Inżynierów Platform/SRE.
    *   **Kryteria Sukcesu**: Pełna audytowalność zapytań (100%), narzut opóźnienia poniżej 15 ms.

---

## 🏢 Rzeczywiste Projekty Wdrożone na Skalę (Publiczne Case Studies)

1.  **MUFG Bank (Racjonalizacja)**:
    *   **Projekt**: Wykorzystanie AI zakotwiczonej w ontologiach (Amazon Neptune i Bedrock) do standaryzacji globalnych procedur operacyjnych i generowania schematów blokowych.
    *   **Rezultat**: **Redukcja o 90%** czasu tworzenia i weryfikacji dokumentacji procesowej (skrócenie z 11 dni roboczych do 1 dnia). [Referencja: AWS Database Blog](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

2.  **Netflix (Architektura Ewolucyjna)**:
    *   **Projekt**: Stratum Resource Tuner (Zautomatyzowane optymalizowanie zasobów kontenerowych na dużą skalę).
    *   **Rezultat**: Ciągłe i autonomiczne dopasowywanie alokacji CPU i pamięci RAM w tysiącach mikroserwisów, eliminujące koszty nadmiarowej rezerwacji infrastruktury chmurowej. [Referencja: Netflix Tech Blog](https://netflixtechblog.medium.com/netflix-stratum-media-processing-automated-container-right-sizing-ddf9aa68a801)

3.  **Capital One (Data & Agentic AI)**:
    *   **Projekt**: Produkcyjne roje agentów dedykowane deterministycznemu wnioskowaniu nad kodem źródłowym (*FinRT*).
    *   **Rezultat**: Przemysłowa automatyzacja audytów bezpieczeństwa i wykrywania podatności w całym bankowym cyklu wytwarzania oprogramowania. [Referencja: Capital One Tech](https://medium.com/capital-one-tech/advancing-safe-agentic-ai-asks-symposium-highlights-bbba40b19784)

4.  **Dynata (Programista Wspomagany)**:
    *   **Projekt**: Wdrożenie metodyki AI-DLC zintegrowanej ze środowiskiem Kiro IDE w rozproszonych zespołach deweloperskich.
    *   **Rezultat**: Dostarczanie złożonych funkcjonalności w **1 sprint zamiast 4** dzięki ciągłej integracji kontekstowej pomiędzy dokumentacją (Jira/Confluence) a bazą kodu. [Referencja: AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/)

---

*Pytanie otwarte dla naszych zespołów na ten tydzień: Czy jesteśmy organizacyjnie przygotowani na to, że nasza kluczowa wartość inżynierska nie będzie już polegać na pisaniu kodu, lecz na orkiestracji, weryfikacji i sterowaniu agentami, którzy ten kod wytwarzają i audytują?*
