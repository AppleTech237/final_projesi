from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
from flask_login import UserMixin
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Modeller
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class urun(db.Model):
    urun_id = db.Column(db.Integer, primary_key=True)
    urun_adi = db.Column(db.String(100), nullable=False)
    aciklama = db.Column(db.Text, nullable=True)
    miktar = db.Column(db.Integer, default=0)
    min_miktar = db.Column(db.Integer, default=0)
    fiyat = db.Column(db.Float, default=0.0)
    kategori = db.Column(db.String(50), nullable=True)
    tedarikci = db.Column(db.String(100), nullable=True)
    konum = db.Column(db.String(100), nullable=True)
    barkod = db.Column(db.String(50), nullable=True)
    urun_resmi = db.Column(db.String(100), nullable=True)
    tarihi_added = db.Column(db.DateTime, default=datetime.utcnow)
    tarihi_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref=db.backref('urunler', lazy=True))

# JSON'a aktarım fonksiyonu
def export_urunler_to_json():
    with app.app_context():
        urunler = urun.query.all()
        
        urunler_data = []
    for n in urunler:
        urunler_data.append({
            "urun_id": n.urun_id,
            "urun_adi": n.urun_adi,
            "aciklama": n.aciklama,
            "miktar": n.miktar,
            "min_miktar": n.min_miktar,
            "fiyat": n.fiyat,
            "kategori": n.kategori,
            "tedarikci": n.tedarikci,
            "konum": n.konum,
            "barkod": n.barkod,
            "image": n.urun_resmi,
            "tarihi_added": n.tarihi_added.isoformat(),
            "tarihi_updated": n.tarihi_updated.isoformat(),
            "user_id": n.user_id
        })
        
        with open('urunler.json', 'w', encoding='utf-8') as file:
            json.dump(urunler_data, file, ensure_ascii=False, indent=4)

        print("Urunler başarıyla urunler.json dosyasına kaydedildi!")

# Ana fonksiyon
if __name__ == '__main__':
    export_urunler_to_json()


