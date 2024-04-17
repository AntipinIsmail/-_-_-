#from forms.register_form import RegisterForm
from forms.user import LoginForm, RegisterForm
from flask import Flask, render_template, url_for, redirect, request
from flask_login import login_user, LoginManager
# , login_required, logout_user, current_user

from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'


#@login_manager.user_loader
#def load_user(user_id):
 #   return User.query.get(int(user_id))


@app.route("/")
def index():
    # user = "Пользователь"
    db_sess = db_session.create_session()
    users = db_sess.query(User).filter().all()
    return render_template('index.html', user=users)

@app.route('/zzzz', methods=['GET', 'POST'])
def registration():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('registration.html', title='Авторизация', form=form)


@app.route('/registration', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user:
            if user.check_password(form.password.data):
               # login_user(user)
               return redirect('/')
    return render_template("login2.html", form=form)




@app.route('/creator', methods=["POST", "GET"])
def creator():
    if request.method == "POST":
        #  user = request.form['product_name']
        return redirect(url_for("home"))
    return render_template('creator.html')


@app.route("/shopping_basket")
def shopping_basket():
    return "<h1> shopping basket</h1>"


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()

