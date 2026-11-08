# **🚀 Ajan Tabanlı AI, Hibrit Bulut ve Rasyonelleştirme: Mimarilerimizi Yeniden Tanımlayan Stratejik Gözlem**

**Bu hafta teknoloji gözlemi, ajan tabanlı AI, BT sistemlerinin rasyonelleştirilmesi ve ölçeklenebilir mimarilerdeki büyük ilerlemeleri vurguluyor.** Otonom ajanların maliyet yönetiminden, iş süreçlerinin ontoloji ile standardizasyonuna ve ajan tabanlı IDE'lerin yükselişine kadar, büyük işletmeler için verimlilik, yönetişim ve dayanıklılık konuları hiç bu kadar kritik olmamıştı.

Netflix, GitHub, AWS ve Capital One'dan gelen deneyimler net bir eğilimi gösteriyor: **AI artık basit bir otomasyon aracı değil, sistemlerimizin merkezi bir aktörü** haline gelmiş durumda ve süreçlerin, mimarilerin ve yetkinliklerin yeniden tasarlanmasını gerektiriyor.

---
---

## **1. 🔄 BT Sistemlerinin Rasyonelleştirilmesi ve Sadeleştirilmesi**

### **İş Süreçlerinin Standardizasyonunda AI'nın Rolü**
Büyük bankacılık ve endüstriyel organizasyonlar, genellikle merkezi olmayan büyümeden kaynaklanan **iş süreçlerinin parçalanması** sorunuyla karşı karşıya kalır. MUFG Bank, bu zorluğu Amazon Neptune ve Bedrock ile entegre **ontoloji tabanlı bir AI çözümü** kullanarak çözdü. Sonuç: **operasyonel prosedürlerin geliştirme süresinde %90'lık bir azalma** (11 adam/günden 1 adam/güne düşüş) ve küresel ölçekte tutarlı bir standardizasyon sağlandı.
→ [Makaleyi okuyun](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

**Neden kritik?**
- **Operasyonel borç**: Parçalanmış süreçler bakımı zorlaştırır ve uyumsuzluk risklerini artırır.
- **Merkezi yönetişim**: Bir iş ontolojisi, **verilere erişimi demokratikleştirirken** kullanımlarını AI tabanlı koruma mekanizmalarıyla kontrol etmeyi sağlar.
- **Anında ROI**: Dokümantasyon ve eğitim maliyetlerindeki azalma, finans yönetimleri için kilit bir argüman.

---
### **Eski Runbook'ların Sonu: Ajan Tabanlı Gözlemlenebilirlik Yolunda**
AI ile hızlanan geliştirme, **manuel runbook'ları güncellenmeden önce eskimiş** hale getiriyor. Sourcegraph radikal bir yaklaşım öneriyor: **derin semantik arama araçları** ve **Model Context Protocol (MCP)** kullanarak olay yönetimini doğrudan mevcut kaynak koduna entegre etmek.
→ [Makaleyi okuyun](https://sourcegraph.com/blog/sre-runbooks-ai-driven-development)

**Neden kritik?**
- **MTTR azaltma**: SRE ekipleri manuel çözüm aramak için daha az zaman harcar.
- **Kararların izlenebilirliği**: Her olay bir kod değişikliğiyle ilişkilendirilir ve tam bir geçmişe sahiptir.
- **Ajanlara uyum**: Sistemler **insanlar yerine otomatik okuyucular** (robotlar/AI) için tasarlanmalıdır.

---
### **Cloud Egemenliği ve Kuantum Sonrası Dönem: Siber Güvenliğin Yeni Sınırları**
Cloudflare, **coğrafi olarak sınırlı anahtar yönetimi** için **kuantum sonrası kriptografi (PQ GeoKey Manager)** kullanan bir çözüm sunuyor. Bu yenilik, **veri egemenliği** ihtiyacına yanıt vererek şifre çözme işleminin yalnızca yetkili coğrafi bölgelerdeki sunucularda gerçekleştirilmesini garanti ediyor.
→ [Makaleyi okuyun](https://blog.cloudflare.com/post-quantum-geo-key-manager/)

**Neden kritik?**
- **Mevzuat uyumu**: GDPR ve AB AI Yasası'na tabi Avrupa bankaları için hayati önem taşır.
- **Gelecekteki saldırılara karşı dayanıklılık**: Kuantum tehditlerine ("harvest now, decrypt later") hazırlık.
- **Tedarik zinciri risklerinin azaltılması**: Güvenilir üçüncü taraflar üzerinde sıkı kontrol.

---
### **AI FinOps: Otonom Ajanların Gerçek Maliyetini Ölçmek**
GitHub Engineering, **araç çağrısı başına yerel token azaltımının**, eksik bağlamı geri almak için AI'nın komutları yeniden başlatmaya zorlaması durumunda verimsiz olabileceğini gösteriyor. Gürültü sıkıştırma ve gereksiz biçimlendirmeyi kaldırma gibi bütüncül bir yaklaşım, **görev kalitesinden ödün vermeden toplam maliyeti optimize eder**.
→ [Makaleyi okuyun](https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/)

**Neden kritik?**
- **Granüler görünürlük**: Token başına maliyet, altyapıyı (hesaplama, soğutma, ağ) içermelidir.
- **Sistemik optimizasyon**: Yerel kazanımlar yeterli değildir; tüm pipeline'ın yeniden düşünülmesi gerekir.
- **Finans yönetimleriyle uyum**: CFO'lar AI yatırımlarını haklı çıkarmak için eyleme geçirilebilir metrikler talep ediyor.

---
---

## **2. 🏗️ Ölçeklenebilir Mimari ve Yazılım Mühendisliği**

### **"Agent-first" Mimariler: BT Altyapısının Temellerini Yeniden Düşünmek**
Microsoft Azure, **ajan tabanlı uygulamaların** (insan müdahalesi olmadan sürekli döngüde çalışabilen) özel bir altyapı gerektirdiğini vurguluyor. **Azure Foundry ve Entra Agent ID** ile sundukları vizyon, ajan mimarilerine büyük işletmelerin talep ettiği titizlik ve uyumu kazandırmayı hedefliyor.
→ [Makaleyi okuyun](https://azure.microsoft.com/en-us/blog/designing-agent-first-platforms-what-changes-when-agents-do-the-work/)

**Neden kritik?**
- **Kimlik ve yönetişim**: Ajanların izlenebilir ve kontrol edilebilir bir kimliğe sahip olması gerekir.
- **Zero Trust güvenliği**: Savunma sınırları araç katmanına taşınmalıdır.
- **Kararların izlenebilirliği**: Bir ajanın her eylemi denetlenmeli ve geri alınabilir olmalıdır.

---
### **Dayanıklılık Sapması: Mimari Diyagramlar Yalan Söylediğinde**
Azure, **"resilience drift"** fenomenini vurguluyor: Sürekli operasyonel değişiklikler teorik diyagramları geçersiz kılar ve **tekil arıza noktalarını** yeniden ortaya çıkarır. Dayanıklılık, **dinamik bir özellik** olarak sürekli ölçülmeli ve doğrulanmalıdır.
→ [Makaleyi okuyun](https://azure.microsoft.com/en-us/blog/your-architecture-diagram-is-not-your-resilience/)

**Neden kritik?**
- **Sürekli doğrulama**: Mimariler üretim ortamında test edilmelidir (örn: chaos engineering).
- **AI modellerine bağımlılık**: Kritik bileşenler artık veri pipeline'larını ve LLM çıkarım süreçlerini içeriyor.
- **İş sürekliliği**: Hata toleransı AI hizmetlerini de kapsamalıdır.

---
### **Çok Bölgeli Dayanıklılık: Hibrit Orkestrasyon Sanatı**
AWS Architecture Blog, **aktif-aktif çok bölgeli** bir mimariyi AWS CloudFormation özel kaynakları için öneriyor. **DynamoDB Global Tables tabanlı dağıtık kilitler** kullanarak çift yürütmeleri önler ve otomatik yük devretme sağlar.
→ [Makaleyi okuyun](https://aws.amazon.com/blogs/architecture/building-multi-Region-resiliency-for-AWS-CloudFormation-custom-resource-deployment/)

**Neden kritik?**
- **Felaket Kurtarma (DR)**: Bankalar kritik uygulamalar için **minimum RTO/RPO** garanti etmelidir.
- **Veri egemenliği**: Hassas veriler hiçbir zaman yetkili bölgeyi terk etmemelidir.
- **Operasyonel basitlik**: Ekipler, karmaşıklık olmadan kurtarma planlarını test edebilmelidir.

---
### **AWS Üzerinde Oracle Database: Kontrollü Hibrit Geçiş**
AWS, **Amazon Elastic VMware Service (EVS)** üzerinde **yüksek erişilebilir Oracle Database 19c** dağıtımını **Amazon FSx for NetApp ONTAP** ile NFS depolama olarak detaylandırıyor. Çözüm, mevcut VMware araçlarını korurken **milisaniyenin altındaki gecikmeler** ve **bölgeler arası felaket kurtarma planı (DRP)** sunar.
→ [Makaleyi okuyun](https://aws.amazon.com/blogs/architecture/architect-highly-available-oracle-database-on-amazon-evs-and-fsx-for-ontap/)

**Neden kritik?**
- **Legacy uyumluluğu**: Bankalar her şeyi yeniden yazma lüksüne sahip değil.
- **Performans ve dayanıklılık**: Finansal işlemler için gecikmeler milisaniyenin altında olmalıdır.
- **Maliyet kontrolü**: Depolama ve yedekleme optimizasyonu operasyonel maliyetleri düşürür.

---
---

## **3. 🧠 Veri ve Ajan Tabanlı AI**

### **GraphRAG: Uyumlulukta Ajan Tabanlı AI'nın Rolü**
Neo4j, **graf tabanlı veritabanlarının** karmaşık finansal dolandırıcılık ağlarını görselleştirmeyi nasıl sağladığını gösteriyor. **Linkurious Enterprise** aracı, Amazon Neptune ile entegre olarak AML (Kara Para Aklamayı Önleme) soruşturmalarını **10 kata kadar hızlandırır** ve varlıklar arasındaki ilişkilerin bütüncül bir görünümünü sunar.
→ [Makaleyi okuyun](https://aws.amazon.com/blogs/database/intuitive-risk-investigation-with-amazon-neptune-and-linkurious-enterprise/)

**Neden kritik?**
- **Nihai faydalanıcıların (UBO) tespiti**: İç içe geçmiş yapılar manuel olarak analiz edilemez.
- **Mevzuat uyumu**: Düzenleyiciler finansal akışların izlenebilirliğini talep ediyor.
- **Ölçeklenebilirlik**: Grafikler **petabaytlarca veriyi** performans kaybı olmadan yönetebilir.

---
### **Text-to-SQL ve Metadata Zenginleştirme: Verilere Erişimi Demokratikleştirmek**
IBM watsonx.data Intelligence, ham veritabanı tablolarını **anlamsal olarak zengin varlıklara** dönüştürmek için metadata zenginleştirme kullanıyor. Çözümleri, FastAPI aracılığıyla doğal dilde veri sorgulamaya olanak tanırken yönetişimi garanti eder.
→ [Makaleyi okuyun](https://medium.com/ibm-data-ai/ibm-watsonx-data-intelligence-metadata-enrichment-text-to-sql-bf03eef1451b)

**Neden kritik?**
- **İş birimlerinin verimliliği**: Finansal analistler veri mühendislerine bağımlı olmadan verilere erişebilir.
- **Silo'ların azaltılması**: İş ontolojisi farklı terminolojileri birleştirir.
- **Uyumluluk**: Zenginleştirilmiş metadata, verilerin kökenini izlemeyi sağlar.

---
### **LLM-as-a-Judge: Ölçekte Otomatik Değerlendirme**
Netflix, bir modelin çıktılarını değerlendirmek için ikinci bir model kullanan **"LLM-as-a-Judge"** tabanlı otomatik bir değerlendirme sistemi uyguladı. **Human-in-the-loop** ve **sürekli izleme** yaklaşımını birleştirerek model sapmalarını önler.
→ [Makaleyi okuyun](https://netflixtechblog.medium.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508)

**Neden kritik?**
- **Ölçeklenebilirlik**: Milyonlarca çıktıyı manuel olarak değerlendirmek imkansızdır.
- **Güvenilirlik**: Değerlendirme modelleri insan beklentileriyle uyumlu olmalıdır.
- **Maliyet azaltma**: Doğrulama için iş birimi uzmanlarına bağımlılığı azaltır.

---
### **AML Soruşturmaları: Uyarıların Ötesinde Parayı İzlemek**
Neo4j, **bilgi grafiklerinin** **Azerbaijani Laundromat** gibi kara para aklama ağlarını yeniden inşa etmeyi nasıl sağladığını açıklıyor. Bu yaklaşım, geleneksel sistemlerle tespit edilemeyen işlem verilerini **bağlamsal istihbarata** dönüştürür.
→ [Makaleyi okuyun](https://neo4j.com/blog/fraud-detection/aml-investigations-following-suspicious-activity-beyond-the-alert/)

**Neden kritik?**
- **AML uyumu**: Bankalar şüpheli akışları takip ettiklerini kanıtlamalıdır.
- **Yanlış pozitiflerin azaltılması**: Grafikler uyarıları bağlamsallaştırmayı sağlar.
- **Hizmetler arası iş birliği**: Uyumluluk ve veri bilimi ekipleri aynı veriler üzerinde çalışır.

## **4. 💻 Geliştirici Ajanı ve Artırılmış Geliştirici**

### **GitHub Copilot SDK for Java: Kurumsal IDE'de Yapay Zeka**
GitHub, **BYOK (Bring Your Own Key)** desteği ile Copilot'ı kurumsal uygulamalara entegre etmek için bir **Java SDK** yayınladı. Bu SDK, Azure, Anthropic veya diğer uç noktalarda barındırılan modellerin kullanılmasını sağlıyor. Modern Java (Jakarta EE 11, Spring) için tasarlanmış olup, **sanal thread'ler** ile ölçeklenebilirliği garanti ediyor.
→ [Makaleyi okuyun](https://github.blog/engineering/using-the-github-copilot-sdk-for-java/)

**Neden kritik?**
- **Model yönetimi**: Bankalar, verilerinin nerede işlendiğini seçebilir.
- **Sorunsuz entegrasyon**: Geliştiriciler IDE değiştirmeden Copilot kullanabilir.
- **Ölçeklenebilirlik**: Sanal thread'ler binlerce eşzamanlı isteği yönetmeyi sağlar.

---
### **Claude Code: Yapay Zeka Çağında Kod İncelemesi**
**Claude Code** ekibi, yüksek hacimli ajanlar tarafından üretilen kodların incelemesini yönetmek için metodolojisini paylaşıyor. Yaklaşımları şunlara dayanıyor:
- **Kapsamlı testler** ile regresyonları en aza indirme.
- **Yüksek riskli alanlar** için stratejik insan odaklı inceleme.
→ [Makaleyi okuyun](https://claude.dev/blog/solving-code-review-at-anthropic/)

**Neden kritik?**
- **Verimlilik vs. Kalite**: Yapay zeka kodlamayı hızlandırır, ancak inceleme bir darboğaz olmaya devam eder.
- **Teknik borcun azaltılması**: Otomatik incelemeler tehlikeli kalıpları tespit eder.
- **Mühendislik kültürü**: Geliştiriciler, yapay zekayı denetlemeyi öğrenmelidir.

---
### **JetBrains Air Governance: IDE'de Ajanları Kontrol Etme**
JetBrains, IDE'lerdeki yapay zeka ajanlarının (Claude, Codex) kullanımını denetlemek için **Air Governance** platformunu tanıtıyor. Bu platform şunları sağlar:
- **Erişim politikaları** tanımlama (hangi modellerin kullanılabileceği).
- **Bütçeleri yönetme** (geliştirici başına maliyet).
- **Verimlilik üzerindeki etkileri analiz etme**.
→ [Makaleyi okuyun](https://blog.jetbrains.com/ai/2026/11/livestream-scaling-agentic-development-with-air-governance/)

**Neden kritik?**
- **Merkezi yönetim**: CIO'lar yapay zeka benimsemesini kontrol etmek ister.
- **Maliyet optimizasyonu**: Premium modellerin (Claude Sonnet 4.5) yüksek maliyeti vardır.
- **DevOps süreçleriyle uyum**: Ajanlar CI/CD pipeline'larına entegre edilmelidir.

---
### **Qodo’s Software Map: Bağımlılıkları Haritalandırarak İncelemeyi İyileştirme**
Qodo, hizmetler arasındaki **dinamik bağımlılık görünümü** ile şunları belirlemeyi sağlar:
- Dağıtımdan önce **riskli alanlar**.
- Kod incelemeleri sırasında tespit edilen **sorun kümeleri**.
→ [Makaleyi okuyun](https://www.qodo.ai/blog/10-ways-qodos-software-map-changes-how-your-team-reviews-plans-and-ships/)

**Neden kritik?**
- **Olayların azaltılması**: Ekipler, değişikliğin etkisini commit'lemeden önce görür.
- **Canlı dokümantasyon**: Harita, kaynak kodla senkronizedir.
- **Ekipler arası işbirliği**: Ürün sahipleri, geliştiriciler ve operasyon ekipleri aynı vizyonu paylaşır.

---
### **Agentic Skill Decay: Yapay Zeka Teknik Uzmanlığı Tehdit Ediyor mu?**
Addy Osmani, **"Skill Decay"** konusunda uyarıyor: Yapay zeka ajanları anlık verimliliği artırsa da, geliştiricilerin **sistemleri derinlemesine anlamasını aşındırabilir**. Otomatik araçlara aşırı bağımlılık, karmaşık hata ayıklamayı ve bakımı zorlaştırabilir.
→ [Makaleyi okuyun](https://addyosmani.com/blog/agentic-skill-decay/)

**Neden kritik?**
- **Uzun vadeli dayanıklılık**: Bankaların legacy kodu anlayabilen geliştiricilere ihtiyacı vardır.
- **Sürekli eğitim**: Ekipler, yapay zekayı denetlemeyi öğrenmeli, ona bağımlı olmamalıdır.
- **İnsan-Yapay Zeka dengesi**: Yapay zeka, insan muhakemesinin yerini almamalı, ona yardımcı olmalıdır.

---
### **Brownfield Agentic Engineering: Legacy Sistemleri Bozmadan Modernleştirme**
Addy Osmani, **legacy kod tabanlarına** yapay zeka geliştirici ajanlarını entegre etmek için pragmatik bir yaklaşım öneriyor. Anahtar, ajanlara **zengin bağlam** sağlamak (RAG veya hassas indeksleme yoluyla), böylece belgelenmesi eski mimarilerde gezinmelerini sağlamaktır.
→ [Makaleyi okuyun](https://addyosmani.com/blog/brownfield-agentic-engineering/)

**Neden kritik?**
- **Büyük teknik borç**: Bankaların kritik eski sistemleri vardır.
- **Operasyonel risk**: Kötü yapılandırılmış bir ajan, iş süreçlerini bozabilir.
- **Kademeli geçiş**: Hizmet kesintisi olmadan modernleştirmek gerekir.

---
### **Beyond the Hallucination: Neden Yapay Zekanın Deterministik Matematiğe İhtiyacı Var?**
Capital One, olasılıksal doğası gereği yapay zeka modellerinin, **mutlak kesinlik gerektiren finansal hesaplamalar** için tek başına kullanılamayacağını gösteriyor. Hibrit mimarileri şunları birleştirir:
- **Keşif katmanı** (sınıflandırma, NLP).
- **Deterministik hesaplama katmanı** (toplama, doğrulama).
→ [Makaleyi okuyun](https://medium.com/capital-one-tech/beyond-the-hallucination-why-ai-needs-deterministic-math-aa9c448479ab)

**Neden kritik?**
- **Veri güvenilirliği**: Hesaplama hataları milyonlara mal olabilir.
- **Regülatif uyum**: Denetçiler izlenebilirlik kanıtı ister.
- **Sağlam mimari**: Yapay zeka, iş birimleri için bir kara kutu olmamalıdır.

---
---

## **5. 🏦 Yapay Zeka ve Bankacılık İş Kolları: Perakende, Varlık Yönetimi ve Yatırım Bankacılığı**

Yapay zeka benimsemesi, finansal kurumlarda artık **genel demonstratörlerin ötesine geçerek**, bankacılığın üç temel sütununun (**Perakende Bankacılığı**, **Varlık Yönetimi** ve **Kurumsal ve Yatırım Bankacılığı - CIB**) değer zincirlerinin merkezine yerleşiyor.

---

### **A. Perakende Bankacılığı (Retail Banking): Kitlesel Otomasyondan Gerçek Zamanlı Hiper-Kişiselleştirmeye**

Perakende bankacılığında, işlemlerin ve müşterilerin büyük hacmi, **olasılıksal yapay zeka modelleri (LLM/SLM)**, deterministik karar motorları ve **Core Banking** ile gerçek zamanlı entegrasyon arasında sıkı bir yakınsama gerektirir.

1. **Anında Kredi Skorlaması ve Artırılmış Onay Süreci**:
   - *Mimari*: Statik skorlama tablolarının yerini, **DSP2 (Açık Bankacılık)** işlem akışları üzerinde eğitilmiş hibrit modeller (Gradient Boosting - XGBoost/LightGBM ve temel modeller) alır. Motor, **EU AI Act** (yüksek risk kategorisi) şeffaflık gereksinimlerini karşılamak için **SHAP**/**LIME** gibi içsel açıklanabilirlik katmanlarını içerir.
   - *Operasyonel etki*: Kişisel krediler ve tüketici kredileri için onay süresi **4 iş gününden 3 dakikanın altına** düşer; **mikro bütçe kırılganlığı sinyallerinin** daha hassas tespiti sayesinde ödeme temerrütlerinde **%18 azalma** sağlanır.

2. **KYC ve Artırılmış Banka Danışmanı için Çok Modlu Ajanlar**:
   - *Mimari*: Gerçek zamanlı belge analizi yapabilen (biyometrik yüz doğrulama, kimlik belgelerinin uyumluluğu, OCR ve görüntü işleme ile vergi beyannamelerinin çıkarımı ve doğrulanması) çok modlu ajanlar. Şube danışmanı tarafında, ajan, müşterinin **360° geçmişini** sentezleyen ve risk profiline en uygun tasarruf veya sigorta ürünlerini öneren bir **"Next Best Action"** yardımcı pilotu olarak çalışır.
   - *Operasyonel etki*: **Periyodik KYC incelemelerine harcanan sürede %65 azalma** ve uyumluluk bozulmadan **müşteri hizmeti taleplerinin %45'i otomatikleştirilir**.

3. **Ultra Hızlı İşlem Dolandırıcılığı Tespiti (Anında Havale ve Kredi Kartı)**:
   - *Mimari*: **Graph Neural Networks (GNN)** ve Apache Kafka/Apache Flink akış pipeline'ları kullanılarak ödeme ağlarının topolojisi **40 milisaniyenin altında** analiz edilir. Sofistike dolandırıcılıklar (CEO dolandırıcılığı, kara para aklama ağları, banka mules) **SEPA anında havalesi** gerçekleşmeden önce engellenir.
   - *Yönetişim ve DORA*: Yerel olarak yedekli çıkarım topolojileri ve engelleme eşiklerinin insan gözetimi ile **operasyonel dayanıklılık** sağlanır.

---

### **B. Varlık Yönetimi: Zayıf Sinyalden Artırılmış Yatırım Tezine**

Varlık ve servet yönetiminde, yapay zeka, portföy yöneticileri ve finansal analistlerin **yapılandırılmamış verilerin patlaması** karşısında bir zeka amplifikatörü olarak işlev görür.

1. **Heterojen Finansal Veriler Üzerinde Artırılmış Araştırma (GraphRAG)**:
   - *Mimari*: Sürekli olarak düzenleyici raporları (SEC 10-K, 10-Q, AMF prospektüsleri), kazanç çağrıları transkriptlerini (Whisper/Mistral Voxtral ile ses transkripsiyonu), haber akışlarını (Bloomberg, Reuters) ve makroekonomik yayınları bağlayan bir **GraphRAG** pipeline'ı. Varlıklar (şirketler, bağlı ortaklıklar, yöneticiler, borçlar, tedarikçiler) **anlamsal bir bilgi grafiğinde** ilişkilendirilir.
   - *Operasyonel etki*: Bir analist, doğal dilde sorgulama yapabilir (*"Avrupa otomotiv tedarikçileri son çeyrek raporlarında hangi tedarik zinciri risklerinden bahsetti?"*) ve **30 saniye içinde** kaynaklı bir sentez notu alabilir; bu, **yatırım komitesi öncesi inceleme süresini 5 kat azaltır**.

2. **Yatırım Tezi Oluşturma ve Makroekonomik Stres Testi**:
   - *Mimari*: Uzmanlaşmış finansal SLM'ler ve kantitatif optimizasyon modelleri (Black-Litterman, Monte Carlo) kombinasyonu. Ajan, kontrafaktüel senaryolar (*"ECB faiz oranlarında 50 baz puan artış ve petrol şoku"*) formüle eder ve portföyün **VaR (Value at Risk)** ve varlık korelasyonları üzerindeki dinamik etkisini projeksiyonlar.
   - *Operasyonel etki*: Piyasa şoklarına karşı daha hızlı tepki ve **yetki altında yönetilen portföylerin** önleyici olarak yeniden dengelenmesi.

3. **ESG Uyumluluğu ve Yeşil Aklama Tespiti**:
   - *Mimari*: İhraççıların metinsel beyanlarının (RSE raporları, CSRD, SFDR Madde 8/9) uydu verileri (metan emisyonları), çevresel cezalar ve STK uyarıları gibi **üçüncü taraf gerçek metriklerle** otomatik olarak karşılaştırılması.
   - *Operasyonel etki*: Sürdürülebilir fonların sınıflandırılmasının güvence altına alınması ve **Avrupa düzenleyicileri (ESMA) tarafından yaptırım riskinin ortadan kaldırılması**.

---

### **C. Kurumsal ve Yatırım Bankacılığı (CIB): Karmaşık Akışların Otomasyonu ve Piyasa Risklerinin Modellemesi**

Finansman ve yatırım bankacılığı, **özel işlemler**, devasa hukuki sözleşme hacimleri ve **salon işlemlerinde yoğun hesaplama** ihtiyaçları ile karakterize edilir.

1. **M&A Anlaşma Yapılandırma ve Kredi Sendikasyonu (LMA Standardı)**:
   - *Mimari*: Finans hukuku ve **Loan Market Association (LMA)** standartlarına uzmanlaşmış sözleşme analizi ajanları. Ajan, yüzlerce sayfalık sözleşmeleri işler, **finansal covenants** (kaldıraç oranları, faiz karşılama), **kontrol değişikliği maddeleri** ve **ön koşulları** otomatik olarak çıkarır; aynı zamanda denetlenebilir bir uyum matrisi üretir.
   - *Operasyonel etki*: M&A due diligence sırasında **sözleşme denetim süresinde %70 azalma**; bankacılık danışmanlarının **kapanışları daha hızlı güvence altına alması** ve **dava risklerini sınırlaması** sağlanır.

2. **Karmaşık Türevlerin Fiyatlandırılması ve Risk Simülasyonlarının Hızlandırılması (Deep XVA)**:
   - *Mimari*: Geleneksel Monte Carlo simülasyonlarının (geceleri devasa sunucu çiftliklerinde çalıştırılan) yerini, **volatilite yüzeylerini ve değerleme ayarlamalarını (CVA/DVA/FVA)** yeniden üretecek şekilde eğitilmiş derin sinir ağları alır.
   - *Operasyonel etki*: Egzotik türev portföyleri üzerindeki XVA hesaplamaları **birkaç saatten onlarca milisaniyeye** düşer; bu, **müşteri görüşmeleri sırasında gerçek zamanlı fiyatlandırma** yapılmasını sağlar.

3. **Piyasa Gözetimi ve Suistimal Tespiti (MAR Yönetmeliği)**:
   - *Mimari*: Emir akışları (FIX protokolü), trader ses kayıtları (güvenli speech-to-text), profesyonel anlık mesajlaşmalar ve haber akışları arasında **gerçek zamanlı çok modlu korelasyon**.
   - *Operasyonel etki*: Anormal davranışların (spoofing, layering, front-running, benchmark manipülasyonu) **proaktif tespiti**; uyum ekiplerinin işlediği **yanlış pozitiflerde %80 azalma**.

4. **Post-Trade Otomasyon ve İşlem Mutabakatı**:
   - *Mimari*: **ISO 20022** standardını uygulayan üçlü mutabakat ajanları (banka, karşı taraf, Euroclear/DTCC merkezi saklama kuruluşları). Ajan, **trade break**'lerin kök nedenini analiz eder ve otomatik olarak düzeltici kayıtlar önerir.
   - *Operasyonel etki*: **CSDR** rejimi altında **cezaların önemli ölçüde azaltılması** ve takas-teslimat süreçlerinin akışkanlaştırılması.

---
---

## **📊 Haftanın Teknik İnfografiği**

![Çubuk grafik, şema düzeltmesi öncesi Agent B, model başına 36 çalıştırma. Şema-geçerli çıktı: Gemini 3.5 Flash için 36'da 30, Gemini 3.8 Flash için 36'da 36. Oracle ile eşleşen durumlar: 36'da 12 ve 13. Ortalama alan-eşleşme skoru: Her ikisi için 0,40.](https://cdn-images-1.medium.com/max/1024/1*JqF2NPBn5wFn8E5h6Y_Gag.png)

**Büyük Bir Banka Grubu İçin Analiz:**

### **Bağlam ve Mimari**
Bu infografik, **Google Cloud** tarafından yapay zeka modellerinin değerlendirilmesine dair bir makaleden alınmıştır ([bağlantı](https://medium.com/google-cloud/a-new-model-is-not-an-upgrade-until-your-evals-say-so-3bdd72d1d97e)). İki modelin (Gemini 3.5 Flash ve 3.8 Flash) performansını şema düzeltmesi öncesi ve sonrası karşılaştırır.

- **Temel bileşenler**:
  - **Agent B**: Model çıktılarını değerlendiren bir yapay zeka ajanı.
  - **Doğrulama şemaları**: Oluşturulan verilerin yapısının kontrolü.
  - **Oracle**: Doğruluk için referans bir gerçek.
  - **Ortalama alan-eşleşme skoru**: Çıktıların oracle ile uyumunu ölçen metrik.

### **Projelerimiz İçin Çıkarımlar**
1. **Yapay Zeka Çıktılarının Güvenilirliği**:
   - Yapay zeka modelleri genellikle **iş şemalarına uygun olmayan veriler** üretir (ör: hatalı biçimlendirilmiş JSON, eksik alanlar).
   - **Çözüm**: Üretimde kullanılmadan önce **deterministik güvenlik önlemleri** (Pydantic, JSON Schema) entegre edilmelidir.

2. **GenAI Gözlemlenebilirliği**:
   - **Ortalama alan-eşleşme skoru**, çıktıların kalitesini ölçmek için kritik bir metriktir.
   - **Bankacılık uygulaması**: Finansal raporlar veya sözleşmeler üreten ajanlar için bu metrik **gerçek zamanlı olarak izlenmelidir**.

3. **GCP/IBM Cloud Üzerinde Ölçeklendirme**:
   - Google Cloud, bu modelleri ölçeklendirmek için **Vertex AI** gibi araçlar sunar.
   - **Öneri**: Kritik sistemlere entegrasyon öncesi yapay zeka çıktılarını doğrulamak için **serverless iş akışları** (Cloud Functions, Cloud Run) kullanılmalıdır.

4. **FinOps ve Maliyetler**:
   - Şema hatalarını düzeltmek için tekrarlanan yapay zeka çağrıları **maliyetleri artırır**.
   - **Optimizasyon**: Modellerin çağrılmasından önce yerel ön doğrulamalar yapılmalıdır.

### **Operasyonel Dersler**
- **LLM'lere körü körüne güvenmeyin**: Çıktıları her zaman **deterministik testlerle** doğrulayın.
- **Değerlendirmeyi otomatikleştirin**: Modelleri dağıtmadan önce **CI/CD pipeline'ları** ile test edin.
- **Ekipleri eğitin**: Geliştiriciler, **modellerin sınırlarını** ve **doğrulama en iyi uygulamalarını** anlamalıdır.

## **🗺️ Haftanın Stratejik Haritası (Wardley Map)**

![Wardley Map - A good enough map](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgdDK7_kvC0fkbYJNouIDIUHo0yfvBugq5bKMmUxavEs3YKYzMNHZok1ibhTtU4jGlaRGeElExA0dVfmajAKTQHNdZJFaQbzx3RgYnMX3z2I0q9KX5ITL5ViB6f6LoXYv2aCslodOxxKJXmZdq0EeL6TBFMWUO-frYqS-M3UDfMe5JgLiodljA1Rg/w400-h145/map04.png)

**Kaynak**: [Simon Wardley - A good enough map](https://blog.gardeviance.org/2024/02/a-good-enough-map.html)

### **Büyük Bir Bankacılık Grubuna Yönelik Stratejik Analiz**

#### **1. Değer Zinciri (dikey eksen)**
- **Son Kullanıcı**: **Standartlaştırılmış iş süreçleri** ve **uyumlu** çözümlere ihtiyaç.
- **İş Süreçleri**: Prosedürlerin standardizasyonu (ör: KYC, AML).
- **Araçlar & Platformlar**: Yapay zeka çözümleri (Amazon Bedrock, watsonx.data).
- **Altyapı**: Bulut (AWS, GCP, Azure), veritabanları (Neptune, FSx for ONTAP).

#### **2. Bileşenlerin Evrimi (yatay eksen)**
| **Bileşen**                 | **Eksen Üzerindeki Konumu** | **Önerilen Strateji**                              |
|-----------------------------|-----------------------------|----------------------------------------------------|
| **İş Süreçleri**            | Ürün → Meta                 | Yapay zeka ile otomatize etme (ör: MUFG Bank).     |
| **İş Ontolojileri**         | Özel → Ürün                 | Amazon Neptune/Bedrock ile endüstrileştirme.      |
| **Yapay Zeka Ajanları**     | Oluşum → Özel               | Güvenlik önlemleri geliştirme (ör: deterministik doğrulama). |
| **Bulut Altyapısı**         | Meta                        | Egemen sağlayıcıları tercih etme (GCP, IBM).       |
| **Gözlemlenebilirlik**      | Ürün → Meta                 | OpenTelemetry ve Instana gibi araçları kullanma.   |

#### **3. Stratejik Hamleler**
- **Çıkarımın Meta Haline Gelmesi**:
  LLM modelleri **meta** haline geliyor (ör: Bedrock, Vertex AI). Bankalar, **model eğitimi** yerine **orkestrasyon** ve **yönetişim**e odaklanmalı.

- **Ontolojilerin Endüstrileşmesi**:
  Bilgi grafikleri (Neo4j, Amazon Neptune), **özel**den **ürün**e geçerek **ölçekte standardizasyon** sağlıyor.

- **Bağımlılık Yönetimi**:
  Ekipler **tekerleği yeniden icat etmekten** kaçınmalı ve yönetilen çözümleri tercih etmeli (ör: watsonx.data ile Text-to-SQL).

#### **4. Bulut (GCP/IBM Cloud) Fırsatları**
- **IBM Cloud**:
  - **watsonx.data** ile veri yönetişimi.
  - **OpenShift** ile hibrit iş yükleri.
- **GCP**:
  - **Vertex AI** ile ajanların dağıtımı.
  - **BigQuery** ile yapay zeka loglarının analizi.

#### **5. Aşılması Gereken Kurumsal Ataletler**
- **Değişime Direnç**: İş birimleri genellikle **manuel runbook**ları tercih ediyor.
- **Legacy Mimari Karmaşıklığı**: Monolitik sistemler, yapay zeka benimsemesini engelliyor.
- **Yetenek Eksikliği**: Veri mühendislerinin **graf ve ontoloji** konularında yetkinliklerini artırması gerekiyor.

## **🚀 3 Ay İçinde Başlatılacak Pilot Projeler**

### **🔹 Pilot Proje #1: İş Süreçlerinin Ontoloji ile Standartlaştırılması (MUFG Bank Tarzı)**
**Amaç**:
**İş ontolojisi + üretken yapay zeka** kombinasyonunun, 10 kişilik bir ekipte operasyonel prosedürlerin (ör: müşteri kabul süreci, AML uyumluluğu) **geliştirme süresini %50 oranında azaltabileceğini** doğrulamak.

**Ekip Kapsamı**:
- 2 backend geliştirici (Java/Spring).
- 1 bulut mimarı (AWS/GCP).
- 1 iş birimi Ürün Sahibi (PO) (bankacılık uyumluluğu).
- 1 veri mühendisi (Neo4j/Amazon Neptune).
- 1 yönetişim uzmanı (RGPD, AB Yapay Zeka Yasası).

**Süre ve Kilometre Taşları**:
- **1. Ay**:
  - Mevcut iş süreçlerinin haritalandırılması (ör: KYC iş akışı).
  - Temel bir ontolojinin **Amazon Neptune** üzerinde dağıtılması.
  - Ontolojiden akış şemaları üreten bir yapay zeka ajanının prototipinin oluşturulması.
- **2. Ay**:
  - Ajanın bir **kurumsal IDE** içine entegrasyonu (ör: VS Code ile GitHub Copilot).
  - 3 gerçek kullanım senaryosu için prosedür üretiminin test edilmesi.
  - Geliştirme süresinin önce/sonra ölçümü.
- **3. Ay**:
  - **Ön üretim ortamına** iş birimi testçileri ile dağıtım.
  - Ekiplerin ontoloji kullanımı konusunda eğitilmesi.
  - Sonuçların yönetime sunulması (YG, maliyet azaltımı).

**Başarı Kriterleri**:
- Prosedür geliştirme süresinde **%30 azalma**.
- Üretilen prosedürlerin **%100’ünün** iş şemalarına uygun olması.
- İş birimi testçilerinin **%80’inden olumlu geri bildirim** alınması.

**Riskler ve Azaltma Stratejileri**:
- **Risk**: Ontoloji eksik veya hatalı modellenmiş olabilir.
  **Azaltma**: Bir **iş uzmanının** sürecin başından itibaren dahil edilmesi ve atölyelerle doğrulama yapılması.
- **Risk**: Ajanlar hatalı prosedürler üretebilir.
  **Azaltma**: Dağıtımdan önce **insan doğrulama katmanı** eklenmesi.

---
### **🔹 Pilot Proje #2: Güvenli Bankacılık Ortamında Ajan Geliştirici (Capital One Tarzı)**
**Amaç**:
Bir **ajan tabanlı IDE (Claude Code/GitHub Copilot)**’ın 10 geliştiricilik bir ekipteki verimlilik üzerindeki etkisini değerlendirmek, aynı zamanda üretilen kodun **güvenliği ve uyumluluğunu** garanti altına almak.

**Ekip Kapsamı**:
- 4 backend geliştirici (Java/Spring, Python).
- 2 frontend geliştirici (React/TypeScript).
- 1 güvenlik mimarı (Zero Trust, mTLS).
- 1 DevOps uzmanı (CI/CD, ArgoCD).
- 1 PO (iş ihtiyaçları ile uyum).
- 1 veri mühendisi (otomatize testler için).

**Süre ve Kilometre Taşları**:
- **1. Ay**:
  - IDE’de **JetBrains Air Governance** veya **GitHub Copilot Enterprise** yapılandırılması.
  - **Güvenlik politikalarının** tanımlanması (ör: hassas müşteri verilerine erişimin engellenmesi).
  - Ekiplerin ajan kullanımı konusunda eğitilmesi (prompt’lar, kod incelemeleri).
- **2. Ay**:
  - Bir **pilot projenin** başlatılması (ör: mevcut bir mikroservisin yeniden yapılandırılması).
  - **Hızın** ölçülmesi (üretilen vs. manuel kod satırları).
  - **Qodo** veya **Sourcegraph Cody** gibi araçlarla kod incelemelerinin otomatize edilmesi.
- **3. Ay**:
  - **Sınırlı üretim ortamına** dağıtım (1 feature flag).
  - **Kalite metriklerinin** analizi (hata sayısı, teknik borç).
  - **FinOps raporunun** sunulması (API çağrı maliyeti vs. verimlilik kazancı).

**Başarı Kriterleri**:
- Tekrarlayan görevlerde **geliştirme süresinde %40 azalma**.
- Üretilen koddan kaynaklanan **0 büyük regresyon**.
- **Maliyet kontrolü**: Bulut maliyetlerinde **%10’dan az artış**.

**Riskler ve Azaltma Stratejileri**:
- **Risk**: Üretilen kod **güvenlik açıkları** içerebilir (ör: SQL enjeksiyonu).
  **Azaltma**: Pipeline’a **güvenlik tarayıcıları** (SonarQube, Snyk) entegre edilmesi.
- **Risk**: Geliştiricilerin **uzmanlık kaybı** yaşaması.
  **Azaltma**: Yapay zeka çıktılarını doğrulamak için **manuel kod inceleme atölyeleri** düzenlenmesi.

---
### **🔹 Pilot Proje #3: IBM Instana & OpenTelemetry ile GenAI Gözlemlenebilirliği**
**Amaç**:
Bir bankacılık ortamında **yapay zeka merkezli gözlemlenebilirlik çözümü** dağıtarak LLM çağrılarının maliyetini, performansını ve kalitesini izlemek.

**Ekip Kapsamı**:
- 2 SRE (Site Reliability Engineer).
- 1 gözlemlenebilirlik mimarı (OpenTelemetry, Prometheus).
- 1 FinOps uzmanı (token başına maliyet).
- 1 veri mühendisi (loglar ve metrikler için).

**Süre ve Kilometre Taşları**:
- **1. Ay**:
  - **IBM Instana GenAI Observability**’nin CI/CD pipeline’ına entegrasyonu.
  - LLM çağrı metriklerinin toplanması için **OpenTelemetry** yapılandırılması.
  - Maliyet veya kalite sapmaları için **uyarıların** tanımlanması.
- **2. Ay**:
  - **Gerçek bir kullanım senaryosu** üzerinde test (ör: müşteri hizmetleri için yapay zeka asistanı).
  - **Token başına maliyet** ve **yanıt süresinin** ölçülmesi.
  - Yönetim için **FinOps raporlarının** otomatize edilmesi.
- **3. Ay**:
  - **Merkezi bir gösterge paneli** ile üretim ortamına dağıtım.
  - Ekiplerin araç kullanımı konusunda eğitilmesi.
  - **Etki raporunun** sunulması (maliyet azaltımı, dayanıklılık iyileştirmesi).

**Başarı Kriterleri**:
- LLM çağrılarıyla ilişkili **maliyetlerde %20 azalma**.
- Yapay zeka ile ilgili olaylar için **MTTR (Ortalama Çözüm Süresi)’nin %30 azaltılması**.
- **Tüm metriklerin (maliyet, gecikme, kalite) %100’ünün** gerçek zamanlı görünür olması.

**Riskler ve Azaltma Stratejileri**:
- **Risk**: Çözüm dağıtımı çok karmaşık olabilir.
  **Azaltma**: Genelleştirmeden önce **sınırlı bir PoC** ile başlanması.
- **Risk**: Metrikler eyleme dönüştürülemez olabilir.
  **Azaltma**: **FinOps ve SRE ekiplerinin** tasarımdan itibaren dahil edilmesi.

---
### **🔹 Pilot Proje #4: Hibrit Oracle Database’den AWS’e Geçiş (FSx for ONTAP ile)**
**Amaç**:
**Kritik bir Oracle Database**’in AWS’e **Amazon FSx for NetApp ONTAP** kullanılarak **hizmet kesintisi olmadan** ve **maliyetlerde %20 azalma** sağlanarak taşınmasını doğrulamak.

**Ekip Kapsamı**:
- 2 veritabanı yöneticisi (DBA).
- 1 bulut mimarı (AWS, VMware).
- 1 felaket kurtarma (DR) uzmanı.
- 1 PO (iş ihtiyaçları ile uyum).

**Süre ve Kilometre Taşları**:
- **1. Ay**:
  - Mevcut Oracle veritabanının **bağımlılıklarının** analizi.
  - **Amazon FSx for ONTAP**’ın yapılandırılması ve performans testleri.
  - **Bölgeler arası replikasyonun** (SnapMirror) planlanması.
- **2. Ay**:
  - **Veri alt kümesinin** test ortamına taşınması.
  - **Gecikme sürelerinin** ve **performansın** doğrulanması.
  - DBAs’lerin yeni altyapı yönetimi konusunda eğitilmesi.
- **3. Ay**:
  - **Trafiğin %10’unun** sınırlı üretim ortamına aktarılması.
  - **Maliyetlerin (depolama, hesaplama)** ve **performansın** ölçülmesi.
  - Yönetime **genelleştirme planının** sunulması.

**Başarı Kriterleri**:
- Kritik işlemler için **gecikme süresi < 1 ms**.
- Depolama ve yedekleme **maliyetlerinde %20 azalma**.
- Taşıma sırasında **0 büyük olay**.

**Riskler ve Azaltma Stratejileri**:
- **Risk**: Performans beklentileri karşılanmayabilir.
  **Azaltma**: Geçişten önce **gerçek yük testlerinin** yapılması.
- **Risk**: Felaket kurtarma (DR) çalışmayabilir.
  **Azaltma**: 3. aydan önce **tam geçiş testinin** simüle edilmesi.

---
### **🔹 Pilot Proje #5: CIB & Sendikasyon Sözleşmelerinin Otomatik Çıkarımı ve Denetimi (LMA Standardı)**
**Amaç**:
Belirleyici güvenlik önlemleri ile donatılmış uzman bir **RAG ajanının**, 150+ sayfalık sendikasyon kredi sözleşmelerindeki (LMA standardı) **finansal covenant’ların %100’ünü** ve kritik maddeleri **%99’dan yüksek doğrulukla** çıkarabileceğini doğrulamak.

**Ekip Kapsamı**:
- 2 backend/IA geliştirici (Python, LangChain, LlamaParse).
- 1 kıdemli CIB finans hukukçusu (finansman dokümantasyonu uzmanı).
- 1 güvenlik ve uyumluluk mimarı (Zero Trust, egemen bulut).
- 1 veri mühendisi (GraphRAG, Neo4j / Amazon Neptune).
- 1 Yapılandırılmış Finansman / Sendikasyon Ürün Sahibi.

**Süre ve Kilometre Taşları**:
- **1. Ay**:
  - Değerlendirme korpusunun oluşturulması (anonimleştirilmiş 50 adet FR/EN çift dilli sendikasyon kredi sözleşmesi).
  - LMA yapısına uygun çok modlu ayrıştırma ve anlamsal bölümlendirme pipeline’ının kurulması.
  - Sözleşme ontolojisinin modellenmesi (kaldıraç oranları, *Negative Pledge*, *Change of Control*, *Events of Default* maddelerinin tanımlanması).
- **2. Ay**:
  - Yapılandırılmış çıkarım için prompt’ların eğitilmesi ve iyileştirilmesi (Pydantic / JSON Schema).
  - Her bir oranın, alıntılandığı sayfa ve kaynak metinle çift yönlü doğrulanması.
  - CIB hukuk ekibi tarafından gerçekleştirilen manuel denetim ile kör benchmark.
- **3. Ay**:
  - CIB deal execution iç portalına entegrasyon.
  - 15 bankacı ve hukukçu ile **gerçek deal koşullarında** dağıtım.
  - DORA / ACPR uyumluluk raporu ve YG hesaplamasının sunulması.

**Başarı Kriterleri**:
- **Due diligence** sırasında **sözleşme denetim süresinde %60 azalma**.
- Test korpusunda **0 kritik covenant atlanması**.
- Hukukçular ve danışman bankacıların **%90’dan fazla memnuniyeti**.

**Riskler ve Azaltma Stratejileri**:
- **Risk**: Özel olarak hazırlanmış maddelerin yanlış yorumlanması veya halüsinasyon.
  **Azaltma**: **Açıklanabilirlik ilkesi**: Her çıkarılan alan için orijinal metnin tıklanabilir şekilde vurgulanması, her closing için **insan onayının zorunlu tutulması** (*Human-in-the-loop*).

## **🏢 Gerçek Dünya Ölçekli Projeler**

### **[Netflix] : Ontology-Driven Observability – Ölçekli Bir Bilgi Grafiği**
**Kategori** : Ölçeklenebilir Mimari & Yazılım Mühendisliği

**Bağlam & İlk Kilitlenme**:
Netflix, **binlerce dağıtık mikroservisi** yöneterek olay teşhisini **son derece karmaşık** hale getiriyor. Geleneksel araçlar (loglar, metrikler, izler) **servisler arası bağımlılıkları** anlamak için yetersiz kalıyor.

**Mimari & Dağıtım**:
- **Bilgi Grafiği**: Servisler arası ilişkilerin açık modellemesi (ör: bağımlılıklar, veri akışları).
- **Ontoloji**: İş kavramlarının tanımlanması (ör: "kritik servis", "finansal akış").
- **Ölçek**: **Milyonlarca düğüm** ve kenar, sorgulama gecikmesi < 100 ms.
- **Araçlar**: Veri depolama için **Neo4j**, veri akışları için **Apache Kafka**.

**Sayısal Etki & Sonuçlar**:
- **MTTR Azaltımı**: Olay çözüm süresi **birkaç saatten** **birkaç dakikaya** indi.
- **Dayanıklılık Artışı**: **Tek hata noktalarının** erken tespiti.
- **Canlı Dokümantasyon**: Harita, **kaynak kodla otomatik senkronize** hale geldi.

**Kamusal Referans**:
[Netflix Tech Blog – Ontology-Driven Observability](https://netflixtechblog.com/ontology-driven-observability-building-an-end-to-end-knowledge-graph-at-netflix-scale-421392cf5adf)

---
### **[Capital One] : Beyond the Hallucination – Hibrit Yapay Zeka + Deterministik Matematik Mimarisi**
**Kategori** : Veri & Agentik Yapay Zeka

**Bağlam & İlk Kilitlenme**:
Capital One, **finansal belgeleri sınıflandırmak** için **LLM'ler** kullanıyor (ör: banka ekstresi), ancak sınıflandırma hataları **düzenleyici veya finansal açıdan büyük etki** yaratabiliyor. Olasılıksal modeller **mutlak doğruluk** garantisi sunmuyor.

**Mimari & Dağıtım**:
- **Yapay Zeka Katmanı**: Varlık çıkarma ve belge sınıflandırma için **LLM'ler**.
- **Deterministik Katman**: Sonuçların **iş kurallarıyla** doğrulanması (ör: tutarlı toplamlar, beklenen formatlar).
- **Ölçek**: **Günde milyonlarca belge** işleme, **yanıt süresi < 500 ms**.
- **Araçlar**: Yönetişim için **IBM watsonx.data**, servis sunumu için **FastAPI**.

**Sayısal Etki & Sonuçlar**:
- **Hata Azaltımı**: Hata oranı **%5'ten** **<%0,1'e** düştü.
- **Uyumluluk Güçlendirme**: Düzenleyiciler için izlenebilirlik kanıtları.
- **Verimlilik Artışı**: Analistler, **zamanlarının %80'ini** düzeltme yerine analiz için harcıyor.

**Kamusal Referans**:
[Capital One Tech – Beyond the Hallucination](https://medium.com/capital-one-tech/beyond-the-hallucination-why-ai-needs-deterministic-math-aa9c448479ab)

---
### **[GitHub] : Git Depolama Mimarisi – Ajanlar Çağına Hazır**
**Kategori** : BT Sistemlerinin Rasyonelleştirilmesi & Basitleştirilmesi

**Bağlam & İlk Kilitlenme**:
GitHub, **saniyede binlerce yazma** ve **isteğe bağlı okuma** işlemini yönetmek zorunda, geliştirme ajanlarının ölçeğini desteklemek için. Eski mimari bir **darboğaz** haline gelmişti.

**Mimari & Dağıtım**:
- **Depolama/Hesaplama Ayrımı**: **Azure Blob Storage** üzerinde sanal replikalar.
- **Koordinasyonun En Aza İndirilmesi**: Gecikmeleri azaltmak için optimize edilmiş yazma işlemleri.
- **Ölçek**: **Milyonlarca depo**, **gecikme < 100 ms**.
- **Araçlar**: Yazma yönetimi için **Spokes** (GitHub'ın dahili sistemi).

**Sayısal Etki & Sonuçlar**:
- **Gecikme Azaltımı**: Okuma süreleri **birkaç saniyeden** **<100 ms'ye** indi.
- **Yatay Ölçeklenebilirlik**: **Kesintisiz** düğüm ekleme imkanı.
- **Yapay Zeka Hazırlığı**: **Otonom kodlama ajanları** için altyapı hazır.

**Kamusal Referans**:
[GitHub Engineering – Inside GitHub’s new Git storage architecture](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/)

---
### **[MUFG Bank] : AI Flowchart – Prosedür Geliştirme Süresinde %90 Azalma**
**Kategori** : Ajan Geliştirici & Artırılmış Geliştirici

**Bağlam & İlk Kilitlenme**:
MUFG Bank, **30 ülkede dağılmış 30.000 operasyonel prosedüre** sahipti; **büyük miktarda tekrarlama** ve **uyumsuzluk riskleri** mevcuttu. Manuel dokümantasyon **eski ve verimsizdi**.

**Mimari & Dağıtım**:
- **İş Ontolojisi**: Süreçlerin **Amazon Neptune** üzerinde modellenmesi.
- **Üretken Yapay Zeka**: Ontolojiden akış şemaları oluşturmak için **Amazon Bedrock**.
- **Ölçek**: **100+ şubede** dağıtım, **geliştirme süresi 11 adam/günden 1 adam/güne** indi.
- **Araçlar**: RAG için **Amazon Bedrock Knowledge Bases**, moderasyon için **Guardrails**.

**Sayısal Etki & Sonuçlar**:
- **Prosedür geliştirme süresinde %90 azalma**.
- **Küresel Standartlaştırma**: **Tüm prosedürler** iş şemalarına uygun.
- **Uyumluluk Kazancı**: Parçalı süreçlerden kaynaklanan **düzenleyici riskler** azaldı.

**Kamusal Referans**:
[AWS Neptune Database Blog – MUFG Bank Case Study](https://aws.amazon.com/blogs/database/how-mufg-bank-aims-to-cut-flowchart-work-by-up-to-90-with-ontology-grounded-ai-on-amazon-neptune-and-amazon-bedrock/)

---
### **[JPMorgan Chase] : LLM Suite & COiN – CIB ve Varlık Yönetimi için Üretken Yapay Zeka Üretimde**
**Kategori** : Yapay Zeka & Bankacılık İş Kolları (Perakende, Varlık Yönetimi & CIB)

**Bağlam & İlk Kilitlenme**:
Kredi sendikasyon sözleşmeleri, ihraç prospektüsleri ve türev anlaşmalarının manuel analizi, her yıl **360.000 saatten fazla** hukukçu ve yatırım bankacısının zamanını alıyordu. İnsan hatası riski ve piyasa işlemlerinin yavaşlığı söz konusuydu.

**Mimari & Dağıtım**:
- **Entegre İç Platform**: *LLM Suite*, güvenli özel bulut üzerinde barındırılan, *COiN* (*Contract Intelligence*) ve CIB ile Varlık Yönetimi işlem sistemlerine entegre bir üretken yapay zeka platformu.
- **Sıkı Güvenlik Önlemleri**: Piyasa ve müşteri verilerinin tam izolasyonu, model sağlayıcı tarafında **sıfır prompt saklama**, SEC ve FINRA uyumu için kriptografik izlenebilirlik ve günlükleme.
- **Ölçek**: Grubun **200.000'den fazla çalışanına**, bunların **60.000'den fazlası** yatırım bankacıları, araştırma analistleri ve varlık yöneticileri dahil, dağıtım.

**Sayısal Etki & Sonuçlar**:
- Kredi sözleşmelerinden **150 temel finansal niteliğin** **birkaç saniye** içinde çıkarılması (sözleşme başına birkaç saat yerine).
- **Yılda 360.000 saat hukuki çalışma tasarrufu**, yüksek katma değerli müzakerelere yönlendirildi.
- **Varlık Yönetiminde araştırma notları hızlandırma**: Finansal sonuçlar konferanslarının (*earnings calls*) sentez süresinde **%75 azalma**.

**Kamusal Referans**:
[JPMorgan Chase Investor & Tech Day – AI & Contract Intelligence (COiN) in Production](https://www.jpmorganchase.com/news-stories/technology-and-innovation-at-jpmorgan-chase)

---
## **🎯 Sonuç: "Agent-Native" Yazılım Mühendisliğine Doğru**

Bu haftaki izleme, **ajan tabanlı yapay zekanın benimsenmesinde benzeri görülmemiş bir hızlanma** olduğunu, ancak aynı zamanda **yönetişim, maliyet ve dayanıklılık açısından büyük zorluklar** olduğunu ortaya koydu.

**BNP Paribas için 3 temel ders:**
1. **Yapay zeka artık bir araç değil, bir aktör**: Otonom ajanlar süreçlerimizi, mimarilerimizi ve yetkinliklerimizi dönüştürüyor. **Sapmaları önlemek için yönetişimi yeniden düşünmek** (FinOps, güvenlik, uyumluluk) gerekiyor.
2. **Rasyonelleştirme bir zorunluluk**: Eski mimariler ve parçalı süreçler, yapay zeka çağıyla uyumsuz. Ontolojiler, bilgi grafikleri ve yönetilen platformlar (AWS, GCP, IBM) **basitleştirme kaldıraçlarıdır**.
3. **Artırılmış geliştirici bir gerçeklik**: Ajan tabanlı IDE'ler (GitHub Copilot, Claude Code) ve otomatik inceleme araçları (Qodo, Sourcegraph) **oyunu değiştiriyor**. Ancak **yeni bir mühendislik kültürü gerektiriyorlar**, burada insan yapay zekayı denetler, tersi değil.

**Tartışma için açık soru:**
*Yapay zeka inovasyonunun aciliyeti ile bankacılık süreçlerinin titizliği nasıl uzlaştırılabilir? Hızlı test için "shadow IT" pilotları mı tercih edilmeli, yoksa baştan itibaren merkezi ve yönetişimli bir yaklaşım mı benimsenmeli?*

---
**📌 Geri bildirimlerinizi yorumlarda veya özel mesajla paylaşın!**
*BNP Paribas için en uygun pilot projeler hangileri sizce?*
*Yapay zeka ajanlarının benimsenmesinde öngördüğünüz engeller neler?*