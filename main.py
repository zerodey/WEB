from flask import Flask
from data import db_session
from sqlalchemy import orm
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

news = orm.relationship("News", back_populates='user')

user = User()
user.name = "Пользователь 1"
user.about = "биография пользователя 1"
user.email = "email@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

news = News(title="Первая новость", content="Привет блог!",
            user_id=1, is_private=False)
db_sess.add(news)
db_sess.commit()


def main():
    db_session.global_init("db/mars_explorer.db")
    # app.run()


if __name__ == '__main__':
    main()