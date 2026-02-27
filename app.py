from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from openai import OpenAI

# ======== إعدادات Flask ========
app = Flask(__name__)
app.secret_key = "supersecretkey"  # ممكن تغيّر
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ======== نموذج قاعدة البيانات ========
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    plan = db.Column(db.String(20), default="basic")
    messages_used = db.Column(db.Integer, default=0)
    message_limit = db.Column(db.Integer, default=100)  # يمكن تغييره حسب الباقة

# ======== Routes ========
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return render_template("index.html")

# ---- تسجيل ----
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        hashed = generate_password_hash(password, method="sha256")
        user = User(username=username, password=hashed)
        try:
            db.session.add(user)
            db.session.commit()
            flash("تم التسجيل بنجاح!", "success")
            return redirect(url_for("login"))
        except:
            flash("اسم المستخدم موجود مسبقاً!", "danger")
            return redirect(url_for("register"))
    return render_template("register.html")

# ---- تسجيل الدخول ----
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for("dashboard"))
        flash("البيانات غير صحيحة", "danger")
        return redirect(url_for("login"))
    return render_template("login.html")

# ---- Dashboard ----
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user = User.query.get(session["user_id"])

    reply = ""
    if request.method == "POST":
        message = request.form['message']

        if user.messages_used >= user.message_limit:
            reply = "لقد استهلكت كل الرسائل في باقتك!"
        else:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "أنت Benidik AI مساعد ذكي يساعد في الأعمال والبرمجة والتطوير."},
                    {"role": "user", "content": message}
                ]
            )
            reply = response.choices[0].message.content
            user.messages_used += 1
            db.session.commit()

    return render_template("dashboard.html", username=user.username, reply=reply, used=user.messages_used, limit=user.message_limit)

# ---- تسجيل الخروج ----
@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("index"))

# ======== Main ========
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)