from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from sqlalchemy.sql import func


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gelistirme_anahtari'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    urunler = db.relationship('urun', backref='owner', lazy=True)

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

    def __repr__(self):
        return f"urun('{self.urun_adi}', '{self.miktar}', '{self.fiyat}')"


class StokIslem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    urun_id = db.Column(db.Integer, db.ForeignKey('urun.urun_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    miktar_change = db.Column(db.Integer, nullable=False)  # + for add, - for remove
    islem_tarihi = db.Column(db.DateTime, default=datetime.utcnow)
    islem_type = db.Column(db.String(20), nullable=False)  # 'add', 'remove', 'update'
    stok_aciklama = db.Column(db.Text, nullable=True)
    
    urun = db.relationship('urun', backref='islemler')
    user = db.relationship('User', backref='stok_islemler')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('E-posta veya şifre hatalı!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST': 
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(email=email).first():
            flash('Bu e-posta zaten kayıtlı!', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        name = request.form.get('name') 
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Kayıt başarılı! Giriş yapabilirsiniz.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():

    # Récup statistq dashbord
    toplam_urunler = urun.query.filter_by(user_id=current_user.id).count()
    low_stok_urunler = urun.query.filter_by(user_id=current_user.id).filter(urun.miktar < 10).count()
    stok_tukendi= urun.query.filter_by(user_id=current_user.id).filter(urun.miktar < 1).count()
    stok_degeri = db.session.query(
        func.sum(urun.miktar * urun.fiyat)
    ).filter_by(user_id=current_user.id).scalar() or 0
    
    
    recent_urunler = urun.query.filter_by(user_id=current_user.id).order_by(urun.tarihi_added.desc()).limit(5).all()
    
    # Récup last transactin
    recent_islemler = StokIslem.query.filter_by(user_id=current_user.id).order_by(StokIslem.islem_tarihi.desc()).limit(5).all()
    

    return render_template('dashboard.html', 
                           adi=current_user.name,
                           toplam_urunler=toplam_urunler,
                           dusuk_stok_sayisi=low_stok_urunler,
                           recent_urunler=recent_urunler,
                           recent_islemler=recent_islemler,
                           stok_degeri=stok_degeri)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/stok_ekle", methods=['GET', 'POST'])
@login_required
def stok_ekle():
    if request.method == 'POST':
        urun_adi = request.form.get('urun_adi')
        aciklama = request.form.get('aciklama')
        miktar = int(request.form.get('miktar', 0))
        fiyat = float(request.form.get('fiyat', 0.0))
        kategori = request.form.get('kategori')
        
        yeni_urun = urun(
            urun_adi=urun_adi,
            aciklama=aciklama,
            miktar=miktar,
            fiyat=fiyat,
            kategori=kategori,
            user_id=current_user.id
        )
        
        db.session.add(yeni_urun)
        db.session.commit()
        
        # İşlemi kaydet
        islem = StokIslem(
            urun_id=yeni_urun.urun_id,
            user_id=current_user.id,
            miktar_change=miktar,
            islem_type='add',
            stok_aciklama=f"İlk ürün eklendi: {urun_adi}"
        )
        db.session.add(islem)
        db.session.commit()
        
        flash('Ürün başarıyla eklendi!', 'success')
        return redirect(url_for('stok_listesi'))
        
    return render_template("stok_ekle.html")

@app.route("/stok_duzenle/<int:urun_id>", methods=['GET', 'POST'])
@login_required
def stok_duzenle(urun_id):
    # Utiliser une variable différente du nom de la classe pour éviter les conflits
    urun_obj = urun.query.get_or_404(urun_id)

    # Vérifier si l'utilisateur est propriétaire du produit
    if urun_obj.user_id != current_user.id:
        flash('Vous n\'êtes pas autorisé à modifier ce produit.', 'danger')
        return redirect(url_for('stok_listesi'))

    if request.method == 'POST':
        ancien_miktar = urun_obj.miktar

        urun_obj.urun_adi = request.form.get('urun_adi')
        urun_obj.aciklama = request.form.get('aciklama')
        urun_obj.miktar = int(request.form.get('miktar', 0))
        urun_obj.fiyat = float(request.form.get('fiyat', 0.0))
        urun_obj.kategori = request.form.get('kategori')
        urun_obj.tarihi_updated = datetime.utcnow()

        db.session.commit()

        # Enregistrer une opération de stock si le montant a changé
        if ancien_miktar != urun_obj.miktar:
            changement = urun_obj.miktar - ancien_miktar
            islem = StokIslem(
                urun_id=urun_obj.urun_id,
                user_id=current_user.id,
                miktar_change=changement,
                islem_type='update',
                stok_aciklama=f"Stock modifié : {urun_obj.urun_adi}"
            )
            db.session.add(islem)
            db.session.commit()

        flash('Produit mis à jour avec succès !', 'success')
        return redirect(url_for('stok_listesi'))

    return render_template("stok_duzenle.html", urun=urun_obj)


@app.route("/stok_listesi")
@login_required
def stok_listesi():
    filtre = request.args.get('filtre')
    urunler = urun.query.filter_by(user_id=current_user.id)

    if filtre:
        filtre = filtre.lower()
        urunler = urunler.filter(
            db.or_(
            (urun.urun_adi.ilike(f"%{filtre}%")) |
            (urun.kategori.ilike(f"%{filtre}%")) |
            (urun.miktar < urun.min_miktar)
        )
        )

    urunler = urunler.order_by(urun.urun_adi).all()
    return render_template("stok_listesi.html", urunler=urunler)


@app.route("/urun_ayrintilari/<int:urun_id>")
@login_required
def urun_ayrintilari(urun_id):
    urun = urun.query.get_or_404(urun_id)

    # Vérifier que l'utilisateur est bien le propriétaire du produit
    if urun.user_id != current_user.id:
        flash('Bu ürünü görüntüleme yetkiniz yok', 'danger')
        return redirect(url_for('stok_listesi'))
    
    # Récupérer l'historique des transactions pour ce produit
    islemler = StokIslem.query.filter_by(urun_id=urun.urun_id).order_by(StokIslem.islem_tarihi.desc()).all()
    
    return render_template("urun_ayrintilari.html", urun=urun, islemler=islemler)

@app.route("/stok_update/<int:urun_id>", methods=['GET', 'POST'])
@login_required
def stok_update(urun_id):
    urun = urun.query.get_or_404(urun_id)
    
    # Vérifier que l'utilisateur est bien le propriétaire du produit
    if urun.user_id != current_user.id:
        flash('Bu ürünü değiştirmenize izin verilmiyor', 'danger')
        return redirect(url_for('stok_listesi'))
    
    if request.method == 'POST':
        action = request.form.get('action')
        miktar = int(request.form.get('miktar', 0))
        stok_aciklama = request.form.get('stok_aciklama', '')
        
        if action == 'add':
            urun.miktar += miktar
            miktar_change = miktar
            islem_type = 'add'
        elif action == 'remove':
            if urun.miktar >= miktar:
                urun.miktar -= miktar
                miktar_change = -miktar
                islem_type = 'remove'
            else:
                flash('Stokta yetersiz miktarda!', 'danger')
                return redirect(url_for('stok_update', urun_id=urun.urun_id))
        else:
            flash('Geçersiz eylem!', 'danger')
            return redirect(url_for('stok_update', urun_id=urun.urun_id))
        
        db.session.commit()
        
        # Enregistrer la transaction
        islem = StokIslem(
            urun_id=urun.urun_id,
            user_id=current_user.id,
            miktar_change=miktar_change,
            islem_type=islem_type,
            stok_aciklama=stok_aciklama
        )
        db.session.add(islem)
        db.session.commit()
        
        flash('Stok başarıyla ayarlandı!', 'success')
        return redirect(url_for('urun_ayrintilari', urun_id=urun.urun_id))
        
    return render_template("stok_update.html", urun=urun)

@app.route("/stok_sil/<int:urun_id>", methods=['POST'])
@login_required
def stok_sil(urun_id):
    urun = urun.query.get_or_404(urun_id)
    
    # Vérifier que l'utilisateur est bien le propriétaire du produit
    if urun.user_id != current_user.id:
        flash('Bu ürünü silmenize izin verilmiyor', 'danger')
        return redirect(url_for('stok_listesi'))
    
    # Supprimer d'abord les transactions associées
    StokIslem.query.filter_by(urun_id=urun.urun_id).delete()
    
    # Ensuite supprimer le produit
    db.session.delete(urun)
    db.session.commit()
    
    flash('Ürün başarıyla kaldırıldı!', 'success')
    return redirect(url_for('stok_listesi'))

@app.route('/hakkinda')
def hakkinda():
    return render_template('hakkinda.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    # app.run(debug=True)
