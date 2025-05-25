#Asagıda sıze verılen sablonu kendı projenıze gore uyarlayarak kendı gıthub projenızın readme.md sı olarak kullanınız.


# 📌 Stok Takip Uygulaması

> Küçük ve orta ölçekli işletmelerin depo ürünlerini takip edebilmeleri için geliştirilmiş bir stok yönetim sistemidir.
---

## 🧾 Proje Tanıtımı

Bu uygulama, depolardaki ürün miktarlarını kontrol etmek, ürünlerin kritik stok seviyelerini belirlemek ve stok giriş-çıkış hareketlerini kaydetmek amacıyla geliştirilmiştir. Flask framework’ü kullanılarak hazırlanmıştır. Kullanıcı girişi, ürün ekleme, stok güncelleme, arama ve raporlama gibi temel işlevleri destekler.

---

## 🚀 Proje Özellikleri

🔐 Yönetici ve depo sorumlusu giriş sistemi (Flask-Login ile)

➕ Ürün ekleme, silme ve güncelleme (CRUD)

🔍 Ürün adı, kategori ve stok miktarına göre filtreleme

⚠️ Kritik seviyeye düşen ürünler için uyarı

🧾 Stok hareketlerinin kayıt altına alınması

📊 Raporlama ve analiz için stok hareket geçmişi

💾 SQLite veya MySQL veritabanı desteği


## ⚙️ Kurulum ve Çalıştırma

### ✅ Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki bileşenlerin bilgisayarınızda kurulu olması gerekir:

Python 3.x

pip

Kullanılan kütüphaneler:

Flask

Flask-Login

SQLAlchemy

WTForms

Bootstrap (arayüz için)

> Not: Bu kütüphaneleri `requirements.txt` dosyasından otomatik olarak yükleyebilirsiniz.

### 🚀 Uygulamayı Başlatma
Örneğin: 
Uygulama tarayıcınızda http://127.0.0.1:5000/ adresinde çalışacaktır.


## 📂 Proje Dosya Yapısı
asagıdakı agacı kendı sıstemınıze gore duzenlemelısınız. bu sadece ornek olarak verılmıstır.
```
├── app.py # Ana Python uygulama dosyası
├── templates/ # HTML şablonlarının bulunduğu klasör
│ ├── index.html # Anasayfa
│ ├── login.html # Giriş formu
│ ├── register.html # Kayıt formu
│ └── dashboard.html # Kullanıcı kontrol paneli
├── static/ # Statik dosyalar (CSS, JS, resimler)
│ └── style.css # Uygulamaya ait stil dosyası
├── requirements.txt # Gerekli Python paketlerini içeren dosya
└── README.md # Proje açıklama dosyası
```















