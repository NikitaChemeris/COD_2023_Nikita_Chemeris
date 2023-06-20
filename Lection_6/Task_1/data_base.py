import sqlite3


def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print("Database connection OK!")
    except Exception as e:
        print(e)
        print("Connection to database failed!")
    return conn


def init_tables(path):
    connection = init_conn(path)
    sql = "CREATE TABLE IF NOT EXISTS news(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, article TEXT NOT NULL, author VARCHAR(50) NOT NULL);"
    connection.execute(sql)
    connection.commit()
    connection.close()


def add_news(path, title, article, author):
    connection = init_conn(path)
    sql = "INSERT INTO news('title', 'article', 'author') VALUES('{}', '{}', '{}')".format(title, article, author)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()


def news_title(path):  # for main page
    connection = init_conn(path)
    sql = "SELECT title FROM news;"
    cursor = connection.cursor()
    cursor.execute(sql)
    values = map(lambda x: x[0], cursor.fetchall())
    connection.close()
    return values


def read_article(path, title):
    connection = init_conn(path)
    sql = "SELECT * FROM news WHERE title = '{}';".format(title)
    cursor = connection.cursor()
    cursor.execute(sql)
    article_data = cursor.fetchone()
    connection.close()
    return article_data
