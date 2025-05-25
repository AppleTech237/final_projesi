#Asagıda sıze verılen sablonu kendı projenıze gore uyarlayarak kendı gıthub projenızın readme.md sı olarak kullanınız.


# 📌 Stok Takip Uygulaması


Render'daki proje bağlantısı
```

```

> Küçük ve orta ölçekli işletmelerin depo ürünlerini takip edebilmeleri için geliştirilmiş bir stok yönetim sistemidir.
---

## 🧾 Proje Tanıtımı

Bu uygulama, depolardaki ürün miktarlarını kontrol etmek, ürünlerin kritik stok seviyelerini belirlemek ve stok giriş-çıkış hareketlerini kaydetmek amacıyla geliştirilmiştir. Flask framework’ü kullanılarak hazırlanmıştır. Kullanıcı girişi, ürün ekleme, stok güncelleme, arama ve raporlama gibi temel işlevleri destekler.

---

## 🚀 Proje Özellikleri

```
🔐 Yönetici ve depo sorumlusu giriş sistemi (Flask-Login ile)

➕ Ürün ekleme, silme ve güncelleme (CRUD)

🔍 Ürün adı, kategori ve stok miktarına göre filtreleme

⚠️ Kritik seviyeye düşen ürünler için uyarı

🧾 Stok hareketlerinin kayıt altına alınması

📊 Raporlama ve analiz için stok hareket geçmişi

💾 SQLite veya MySQL veritabanı desteği
```

## ⚙️ Kurulum ve Çalıştırma

### ✅ Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki bileşenlerin bilgisayarınızda kurulu olması gerekir:

```
Python 3.x

pip

Kullanılan kütüphaneler:

Flask

Flask-Login

SQLAlchemy

WTForms

Bootstrap (arayüz için)
```

### 🚀 Uygulamayı Başlatma
Proje klasörüne terminal ile gidin ve aşağıdaki komutu çalıştırın:

```
python app.py
```
Uygulama tarayıcıda şu adreste çalışacaktır: http://127.0.0.1:5000


## 📂 Proje Dosya Yapısı
```
├──────── 2.hafta                       # Projet dosyası
│      ├───── instance/                 # Yerel yapılandırma veya veritabanı dosyaları
│      │
│      ├───── static/
│      │   └── images/                  # Uygulamada kullanılan görseller
│      │       └── hero.png
│      ├───── templates/                # Uygulamanın HTML şablon dosyaları
│      │   ├── base.html                # Diğer sayfalar tarafından kullanılan temel şablon
│      │   ├── dashboard.html           # Giriş yaptıktan sonra kullanıcı paneli
│      │   ├── hakkinda.html            # Hakkında sayfası
│      │   ├── index.html               # Ana sayfa
│      │   ├── login.html               # Giriş yapma sayfası
│      │   ├── register.html            # Kayıt olma sayfası
│      │   ├── stok_duzenle.html        # Ürün düzenleme sayfası
│      │   ├── stok_ekle.html           # Yeni ürün ekleme sayfası
│      │   └── stok_listesi.html        # Stoktaki ürünlerin listesi
│      │
│      ├── app.py                       # Flask uygulamasının ana dosyası
│      ├── db2json.py                   # Veritabanını JSON formatına aktaran script
│      ├── urunler.json                 # Ürünlere ait örnek JSON verisi
│      ├── users.json                   # Kullanıcılara ait örnek JSON verisi
│      ├── requirements.txt             # Gerekli Python kütüphaneleri listesi
│      └── README.md                    # Proje açıklama dosyası
└── final_versiyon.md            # Final sürüm açıklama dosyası
```














