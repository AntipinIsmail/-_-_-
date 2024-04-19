from flask import Flask, render_template, url_for, redirect, request, flash, send_from_directory
from flask_login import login_user, LoginManager, login_required, logout_user, current_user
from flask_uploads import UploadSet, IMAGES, configure_uploads

from data import db_session
from data.users import User
from data.items import Items
from forms.user import LoginForm, RegisterForm
from forms.Item import AddItem


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'

photos = UploadSet("photos", IMAGES)
configure_uploads(app, photos)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/test')
def test():
    items = [{'name': 'Забавная футболка', 'description': 'Очень крутая футболка с забавным принтом',
              'price': 1000, 'image': '/static/images/1.png'}]
    return render_template('test.html', items=items)


@app.route("/", methods=['GET', 'POST'])
def index():
    db_sess = db_session.create_session()
    users = db_sess.query(Items).filter().all()
    for elem in users:
        print(type(elem.picture))
    return render_template('test.html', user=users)


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
                login_user(user)
                return redirect('/')
            else:
                flash('incorrect password!')
                return render_template('login2.html', form=form)
        else:
            flash('incorrect email!')
            return render_template('login2.html', form=form)
    return render_template("login2.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/uploads/<filename>")
def get_file(filename):
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"], filename)


@app.route('/creator', methods=["POST", "GET"])
@login_required
def creator():
    form = AddItem()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = url_for('get_file', filename=filename)
        print(file_url)
        print(filename)
        db_sess = db_session.create_session()
        item = Items(name=form.item_name.data,
                     about=form.about.data,
                     price=form.price.data,
                     picture=file_url,
                     user_id=current_user.id,
                     )
        db_sess.merge(current_user)
        db_sess.add(item)
        db_sess.commit()
        return redirect("/")
    else:
        file_url = None
    return render_template("creator.html", form=form, file_url=file_url)


@app.route('/cart')
@login_required
def cart():  # Пример, потом сюда свои данные закинем
    cart_items = [
        {'name': 'Item 1', 'price': 10, 'producer': 'John'},
        {'name': 'Item 2', 'price': 20, 'producer': 'Mike'},
        {'name': 'Item 3', 'price': 30, 'producer': 'Kolya'}
    ]
    total = sum(item['price'] for item in cart_items)

    return render_template('cart.html', cart_items=cart_items, total=total)


# @app.route("/test")
# def test():
#   db_sess = db_session.create_session()
#  users = db_sess.query(User).filter().all()
# return render_template('index.html', user=users)


@app.route("/shopping_basket")
def shopping_basket():
    return "<h1> shopping basket</h1>"


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
