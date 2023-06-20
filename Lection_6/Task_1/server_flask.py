from flask import Flask, render_template, redirect, request, url_for
from data_base import *

db_path = "news.db"

servak = Flask(__name__)
init_tables(db_path)


@servak.route('/')
def index():
    title_news = news_title(db_path)
    return render_template('main.html', title_news=title_news)


@servak.route('/writing', methods=['POST'])
def add_items():
    title_input = request.form['title']
    article_input = request.form['article']
    author_input = request.form['author']
    add_news(db_path, title_input, article_input, author_input)
    return redirect('/', code=302)


@servak.route('/reading')
def reading():
    name = request.args.get('name')
    return render_template('reading_news.html', name=read_article(db_path, name))


@servak.route('/redirect_add')
def redirect_write():
    return render_template('add_news.html')


if __name__ == '__main__':
    servak.run(host='0.0.0.0', port=8081)
