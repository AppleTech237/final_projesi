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
        urunler = urun.query.filter_by(user_id=current_user.id).all()
        
        urunler_data = []
    for urun in urunler:
        urunler_data.append({
            "urun_id": urun.urun_id,
            "urun_adi": urun.urun_adi,
            "aciklama": urun.aciklama,
            "miktar": urun.miktar,
            "min_miktar": urun.min_miktar,
            "fiyat": urun.fiyat,
            "kategori": urun.kategori,
            "tedarikci": urun.tedarikci,
            "konum": urun.konum,
            "barkod": urun.barkod,
            "image": urun.urun_resmi,
            "tarihi_added": urun.tarihi_added.isoformat(),
            "tarihi_updated": urun.tarihi_updated.isoformat()
        })
        
        with open('urunler.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Urunler başarıyla urunler.json dosyasına kaydedildi!")

# Ana fonksiyon
if __name__ == '__main__':
    export_urunler_to_json()


