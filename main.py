from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    return "<h1> hello wORLD </h1>"


@app.route("/login")
def login():
    return "<h1> loamdfniasn</h1>"


@app.route("/register")
def register():
    return "<h1> loface</h1>"


def main():
    # db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
