from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models import Article, Author

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/', methods=['GET'])
def article_list():
    articles: Article = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )


@article.route('/<int:article_id>/', methods=['GET'])
def article_detail(article_id):
    _article: Article = Article.query.filter_by(id=article_id).one_or_none()
    if _article is None:
        raise NotFound
    return render_template(
        'articles/details.html',
        article=_article,
    )


@article.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template('articles/create.html', form=form)


@article.route('/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    if form.validate_on_submit():
        _article = Article(title=form.title.data.strip(), text=form.text.data)
        if current_user.author:
            _article.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            _article.author_id = author.id

        db.session.add(_article)
        db.session.commit()

        return redirect(url_for('article.article_detail', article_id=_article.id))

    return render_template('articles/create.html', form=form)
