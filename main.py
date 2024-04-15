from flask import Flask, render_template, redirect
from forms.register_form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    user = "Пользователь"
    return render_template('index.html', title='Домашняя страница', username=user)


@app.route("/login")
def login():
    return "<h1> loamdfniasn</h1>"


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('registration.html', title='Авторизация', form=form)


@app.route("/desing")
def desing():
    return "<h1> desing</h1>"


@app.route("/shopping_basket")
def shopping_basket():
    return "<h1> shopping basket</h1>"


@app.route('/success')
def success():
    return "Успешная регистрация!"


def main():
    # db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
