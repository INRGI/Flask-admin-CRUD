from flask import Blueprint, render_template
from models import db
from models import Article

article_page = Blueprint('article_page', __name__,
                        template_folder='templates')

@article_page.route('/<int:article_id>')
def get_article(article_id):
    article = Article.query.filter(Article.id == article_id).first()
    return render_template('article.html',article=article)
