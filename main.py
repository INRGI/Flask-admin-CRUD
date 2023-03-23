from flask import Flask,render_template,session, Blueprint
from models import db
from models import Article
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from dotenv import load_dotenv
import os
from article_part import article_page
from flask_session import Session

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.config['FLASK_ADMIN_SWATCH'] = os.environ["ADMIN_THEME"]
app.secret_key = os.environ["SECRET_KEY"]
app.config['SESSION_TYPE'] = os.environ["SESSION_TYPE"]

sess = Session()
sess.init_app(app)

app.register_blueprint(article_page,url_prefix='/articles')

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    articles = Article.query.all()
    return render_template('index.html', articles=articles)

@app.route('/<int:article_id>')
def one_article(article_id):
    article = Article.query.filter(Article.id == article_id).first()
    return render_template('article.html',article=article)

admin = Admin(app, name='Адмін панель', template_mode='bootstrap3')
admin.add_view(ModelView(Article, db.session))

app.run()
