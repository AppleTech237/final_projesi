from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Modelin (aynı şekilde)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

def export_users_to_json():
    with app.app_context():
        users = User.query.all()
        data = []
        for user in users:
            data.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'password': user.password  # şifreler hashli şekilde yazılır, düz şifre değil-database baz alınarak
            })
        
        with open('users.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Kullanıcılar başarıyla users.json dosyasına kaydedildi!")

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
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


if __name__ == '__main__':
    export_users_to_json()
