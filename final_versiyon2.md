
📌 Stok Takip Uygulaması
Küçük ve orta ölçekli işletmelerin depo ürünlerini takip edebilmeleri için geliştirilmiş bir stok yönetim sistemidir.

🧾 Proje Tanıtımı
Bu uygulama, depolardaki ürün miktarlarını kontrol etmek, ürünlerin kritik stok seviyelerini belirlemek ve stok giriş-çıkış hareketlerini kaydetmek amacıyla geliştirilmiştir. Flask framework’ü kullanılarak hazırlanmıştır. Kullanıcı girişi, ürün ekleme, stok güncelleme, arama ve raporlama gibi temel işlevleri destekler.

🚀 Proje Özellikleri
🔐 Yönetici ve depo sorumlusu giriş sistemi (Flask-Login ile)

➕ Ürün ekleme, silme ve güncelleme (CRUD)

🔍 Ürün adı, kategori ve stok miktarına göre filtreleme

⚠️ Kritik seviyeye düşen ürünler için uyarı

🧾 Stok hareketlerinin kayıt altına alınması

📊 Raporlama ve analiz için stok hareket geçmişi

💾 SQLite veya MySQL veritabanı desteği

⚙️ Kurulum ve Çalıştırma
✅ Gereksinimler
Bu projeyi çalıştırmak için aşağıdaki bileşenlerin bilgisayarınızda kurulu olması gerekir:

Python 3.x

pip

Kullanılan kütüphaneler:

Flask

Flask-Login

SQLAlchemy

WTForms

Bootstrap (arayüz için)

Not: Tüm kütüphaneleri requirements.txt dosyası üzerinden aşağıdaki komutla yükleyebilirsiniz:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Uygulamayı Başlatma
Proje klasörüne terminal ile gidin ve aşağıdaki komutu çalıştırın:

bash
Copy
Edit
python app.py
Uygulama tarayıcıda şu adreste çalışacaktır:
http://127.0.0.1:5000

📂 Proje Dosya Yapısı
csharp
Copy
Edit
├── app.py                   # Ana uygulama dosyası
├── templates/               # HTML şablonlarının bulunduğu klasör
│   ├── login.html           # Giriş formu
│   ├── register.html        # Kayıt formu
│   ├── dashboard.html       # Ana kontrol paneli
│   ├── urun_ekle.html       # Ürün ekleme sayfası
│   └── stok_listesi.html    # Ürün listeleme ve filtreleme
├── static/                  # CSS, JS ve görseller
│   └── style.css
├── models.py                # Veritabanı modelleri
├── forms.py                 # Form tanımları (WTForms)
├── requirements.txt         # Kullanılan kütüphaneler
└── README.md                # Bu dosya
🎥 Ekran Görselleri / Kısa Demo
Sistemin kullanıcı giriş ekranı, ürün ekleme, stok güncelleme ve raporlama ekranlarının görselleri screenshots/ klasöründe yer almaktadır.

Veritabanı içeriği JSON formatında data_export.json olarak dışa aktarılmıştır.

Proje tanıtım videosu (Drive bağlantısı): Drive Videosu

🧠 Zorluklar ve Öğrenilenler
Flask ile kullanıcı oturumu yönetimi ilk başta karmaşık görünse de araştırma ve örnek projelerle çözüldü.

Veritabanı ilişkileri (örneğin: ürünler ve stok hareketleri) hakkında pratik kazanıldı.

Formlardan gelen verilerin doğruluğunu kontrol etmenin ne kadar önemli olduğu fark edildi.

Gerçek dünyada bir sistem kurmanın sadece kod yazmakla sınırlı olmadığı, planlama ve hata yönetiminin de çok önemli olduğu öğrenildi.

🔧 Geliştirilebilir Yönler
Ürünlerin görsellerini yükleyebilme

Yetki seviyesi yüksek kullanıcılar için detaylı raporlar

E-posta ile düşük stok uyarı sistemi

Birden fazla depo desteği

QR kod entegrasyonu ile hızlı ürün takibi

📬 İletişim
GitHub Reposu: github.com/kullaniciadi/stok-takip


