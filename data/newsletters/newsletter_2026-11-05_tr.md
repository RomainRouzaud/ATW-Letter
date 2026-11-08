# Teknoloji Bülteni #124: Ajanik Mimari ve Artırılmış Mühendislik Çağı

Bu hafta teknoloji takibimiz, yazılım mühendisliği ve kurumsal mimari pratiklerimizde belirleyici bir dönüşümü teyit ediyor: basit sohbet tabanlı denemelerden **endüstriyel ajan mühendisliğine** geçiyoruz. Odak noktası artık yalnızca kod üretimi değil; kurumsal yönetişim (governance), birim maliyet ekonomisi (FinOps) ve karmaşık dağıtık sistemlerdeki bağımlılık zincirlerinin kontrol altına alınmasıdır.

---

## 1. 🔄 BT Sistemlerinin Rasyonelleştirilmesi ve Basitleştirilmesi
Netflix ve Cloudflare'in son mühendislik deneyimlerinden çıkarılacak temel ders gayet açık: yüksek performans sadeliğin bir fonksiyonudur. Cloudflare, düşük seviyeli algoritmik optimizasyonlarla (Rust ile uygulanan tutarlı özetleme - consistent hashing) 100 TB'ın üzerinde RAM tasarrufu sağlarken; Netflix, Apache Flink otomatik ölçeklendirme sistemlerini açık kaynak topluluk standartlarına uyarlayarak yeniden yapılandırıyor. Büyük bir bankacılık grubu için bu durum, kurum içi özel bileşenlerin kontrolsüz çoğalmasını ("kendi bünyesinde geliştir vs. benimse") durdurmanın ve sağlam, standartlaştırılmış temellere odaklanmanın hayati önemini bir kez daha ortaya koyuyor.

*   [Cloudflare'de Bellek Optimizasyonu](https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/)
*   [Netflix'te Apache Flink Otomatik Ölçeklendirme](https://netflixtechblog.com/a-tale-of-two-flink-autoscalers-e9f6a1b1492b)

## 2. 🏗️ Evrimsel Mimari ve Yazılım Mühendisliği
**AI Ağ Geçitleri (AI Gateways)** ve **Model Bağlam Protokolü (MCP)**'nün yükselişi, kurumsal mimarimiz için en kritik temel konudur. Bu mimari kalıplar, yapay zeka modellerini operasyonel uygulamalardan ayrıştırarak; denetim, mevzuata uyumluluk, telemetri ve güvenlik için merkezi bir kontrol düzlemi sağlar. Ayrıca MCP protokolünün *durumsuz (stateless)* mimarilere geçişi, sunucusuz dağıtımlar (AWS Lambda, Bedrock) için kilit bir fırsat sunarak karmaşık oturum yönetimi olmadan yatay ölçeklenebilirlik sağlar.

*   [Yapay Zekayı Yönetmek İçin Evrimsel Mimari Kalıpları](https://www.infoq.com/articles/evolutionary-architecture-pattern/)
*   [MCP Durumsuz Mimariye Geçti: Sunucusuz Ajan Dağıtımları](https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/)

## 3. 🧠 Veri ve Ajanik Yapay Zeka (Agentic AI)
Veri temel yakıt olmaya devam ediyor, ancak yapısı artık otonom ajanların gereksinimleri doğrultusunda şekilleniyor. **GraphRAG** (Amazon Neptune gibi grafik veritabanlarının LLM'lerle entegrasyonu) üzerine saha geri bildirimleri, iş modelleme eforlarında %90'a varan çarpıcı bir düşüş gösteriyor. LLM'leri titiz iş ontolojilerine bağlayarak halüsinasyon risklerini ortadan kaldırıyor ve KYC/AML süreçlerimizde zorunlu olan yasal uyumluluğu garanti altına alıyoruz.

*   [MUFG Bank: Süreç Modellemesinde %90 Zaman Tasarrufu](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)
*   [Bağlamsal Bilgi Alma ve GraphRAG](https://neo4j.com/blog/agentic-ai/contextual-retrieval/)

## 4. 💻 Geliştirici Ajanı ve Artırılmış Geliştirici (Augmented Developer)
**Artırılmış yazılım mühendisliği** çağına resmen adım atıyoruz. Ajanlar artık yalnızca kod tamamlama araçları değil, tam teşekküllü süreç orkestratörleridir (örn. Claude Code, Qodo).

*   **Üretkenlik Paradoksu**: GitHub Copilot (Java için özel SDK'sı aracılığıyla) ve Cursor gibi ajanik IDE'ler yazılım geliştirmenin doğasını değiştiriyor. Operasyonel darboğaz kod yazmaktan kod incelemeye, mimari doğrulamaya ve gerileme (regression) testlerine kaydı.
*   **Yönetişim ve Güvenlik**: Ajanlar tarafından otomatik kod incelemesi ve test üretimi (örn. Google Mantis, Qodo) artık zorunlu bir operasyonel standarttır. Bununla birlikte *Skill Decay* (teknik beceri erozyonu) riskine karşı tetikte kalmalıyız: yapısal mimariyi doğrulamak için insan mimar ve mühendis mutlaka dümende kalmalıdır.
*   **Altyapı Evrimi**: GitHub ve Anthropic, kod depolarını kilitlemeden sürekli kod yazıp teslim eden otonom ajanları desteklemek için sürüm kontrol mantığını baştan tanımlıyor.

*   [Java için GitHub Copilot SDK](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)
*   [JetBrains Air Governance ile Geliştirici Ajanlarının Yönetişimi](https://blog.jetbrains.com/ai/2026/11/livestream-scaling-agentic-development-with-air-governance/)

---

## 📊 Haftanın Teknik İnfografiği

![Deterministik Testlerle Yapay Zeka Modellerinin Doğrulanması (Google Cloud/Vertex AI)](https://cdn-images-1.medium.com/max/1024/1*L-sfIHDoKW1COd8Dyq7Pkg.png)

*Kaynak: [Google Cloud Community - A New Model Is Not an Upgrade Until Your Evals Say So](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e)*

**Mimari Analiz**: Bu şema, yeni model sürümlerini devreye alırken deterministik değerlendirme paketlerinin (sıkı Pydantic şemalarına ve programatik doğrulama kapılarına dayalı) hayati önemini göstermektedir. Şema kontrolleri uygulanmadan önce iş kurallarına uyum dalgalıydı; kontrollerin devreye alınmasının ardından sistemin güvenilirliği belirgin biçimde sıçrama yaptı.
**Operasyonel Çıkarım**: Otonom bir ajanı yapısal doğrulama ve kanarya testleri olmadan asla canlı ortama almayın. Bankacılık ve finans alanında işlem veri formatını halüsinasyonla bozan bir ajan kritik bir operasyonel risk teşkil eder.

---

## 🗺️ Haftanın Stratejik Haritası (Wardley Map)

![Wardley Map - Uygulama Geliştirme Yığını ve Sunucusuz (Serverless) Mimarinin Evrimi](https://cdn-images-1.medium.com/max/1024/1*-oZD4wPJkqOPQbuLPSCF0Q.jpeg)

*Kaynak: [Simon Wardley — On playing chess (Wardley Maps Publication)](https://medium.com/wardleymaps/on-playing-chess-2634b825dbac)*

**Stratejik Analiz**: Bu harita, modern yazılım mühendisliğindeki ağırlık merkezinin köklü değişimini göstermektedir: işlem gücünün ve çalışma zamanı ortamlarının kamu hizmeti niteliğindeki emtialara (*Commodity/Utility* - Sunucusuz mimariler ve yönetilen platformlar) dönüşmesiyle birlikte, alt seviye altyapı geliştiriciler için tamamen şeffaf hale gelir. Geçmişte *Yak Shaving* (sunucu tedariki, işletim sistemi yamaları, kapasite planlaması) nedeniyle kaybedilen mühendislik eforu, doğrudan kullanıcıya yönelik iş mantığına aktarılır.
**Stratejik Hamle**: Kodlama ajanlarının ve ajanik IDE'lerin yükselişiyle birlikte, kod yazımının kendisi de endüstriyel bir emtia haline gelmektedir. Üst düzey mimarların ve kurumsal mühendislerin stratejik değeri değer zincirinin en tepesine kaymaktadır: çoklu ajan orkestrasyonu, bağlam sınırları, güvenlik denetimleri ve uçtan uca kurumsal mimari uyumu.

---

## 🚀 3 Ay İçinde Başlatılacak Pilot Projeler

1.  **Yönetilen Geliştirici Ajanı Pilotu**:
    *   **Hedef**: Eski (legacy) bir depoda maliyet ve güvenlik politikalarını denetlemek üzere *Air Governance* eşliğinde ajanik bir IDE'nin (Cursor/Continue) kontrollü kullanımını doğrulamak.
    *   **Kapsam**: Yaklaşık 10 kişilik 1 mühendislik ekibi.
    *   **Aşamalar**: M1 (Kurulum ve Güvenlik Kuralları), M2 (Hedefli Bakım Görevleri), M3 (Üretkenlik ve Kod Kalitesi Ölçümü).
    *   **Başarı Kriterleri**: Hata ayıklama süresinde %20 azalma, belirlenen belirteç (token) bütçesine tam uyum.

2.  **Uyum için GraphRAG Pilotu**:
    *   **Hedef**: Yapılandırılmamış KYC belgelerinden Nihai Gerçek Faydalanıcı (UBO) tespitini Amazon Neptune ve Bedrock kullanarak otomatikleştirmek.
    *   **Kapsam**: 1 Veri Mühendisi, 1 Veri Bilimci, 1 Mevzuat Uyum Uzmanı.
    *   **Başarı Kriterleri**: Manuel denetimlere kıyasla > %95 doğruluk ve kapsayıcılık.

3.  **Kurumsal AI Gateway Pilotu**:
    *   **Hedef**: Semantik yönlendirme, maliyet takibi ve içerik denetimi sağlamak için tüm şirket içi LLM çağrılarını merkezi bir AI Gateway üzerinden toplamak.
    *   **Kapsam**: 1 Çözüm Mimarı, 2 Platform/SRE Mühendisi.
    *   **Başarı Kriterleri**: İsteklerde %100 görünürlük, < 15ms ek gecikme maliyeti.

---

## 🏢 Ölçeklenmiş Gerçek Projeler ve Kamuoyu Vaka Analizleri

1.  **MUFG Bank (Rasyonelleştirme)**:
    *   **Proje**: Küresel iş süreçlerinin standardizasyonu ve akış şeması üretimi için ontolojiye dayalı yapay zeka (Amazon Neptune & Bedrock).
    *   **Ölçülebilir Sonuç**: Dokümantasyon hazırlama sürelerinde **%90 azalma** (11 iş gününden yalnızca 1 güne indi). [Referans: AWS Database Blog](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

2.  **Netflix (Evrimsel Mimari)**:
    *   **Proje**: Stratum Resource Tuner (Büyük ölçekte otomatik konteyner boyutlandırma).
    *   **Ölçülebilir Sonuç**: Binlerce mikroserviste CPU ve bellek tahsislerinin sürekli ve otonom optimize edilmesi, gereksiz kaynak ayırma maliyetlerini ortadan kaldırdı. [Referans: Netflix Tech Blog](https://netflixtechblog.medium.com/netflix-stratum-media-processing-automated-container-right-sizing-ddf9aa68a801)

3.  **Capital One (Veri ve Ajanik Yapay Zeka)**:
    *   **Proje**: Kaynak kod üzerinde deterministik ve güvenilir akıl yürütme için üretimde çalışan ajan sürüleri (*FinRT*).
    *   **Ölçülebilir Sonuç**: Bankacılık yazılım teslim döngüsünde otomatik güvenlik taramalarının ve zafiyet tespitinin endüstriyel standart haline getirilmesi. [Referans: Capital One Tech](https://medium.com/capital-one-tech/advancing-safe-agentic-ai-asks-symposium-highlights-bbba40b19784)

4.  **Dynata (Artırılmış Geliştirici)**:
    *   **Proje**: Dağıtık ekiplerde Kiro IDE ortamıyla entegre AI-DLC metodolojisinin benimsenmesi.
    *   **Ölçülebilir Sonuç**: Proje dokümantasyonu (Jira/Confluence) ile kaynak kod arasındaki gerçek zamanlı bağlamsal entegrasyon sayesinde karmaşık özelliklerin **4 sprint yerine 1 sprintte** teslim edilmesi. [Referans: AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/how-dynata-scaled-ai-across-the-development-lifecycle-with-ai-dlc-and-kiro-ide/)

---

*Bu hafta ekiplerimiz için açık soru: Yarınki temel mühendislik katma değerimizin artık kod yazmakta değil; kodu üreten ve denetleyen ajanları yönetmekte, doğrulamakta ve yönlendirmekte yattığını kabul etmeye hazır mıyız?*
