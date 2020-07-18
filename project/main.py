import os
from logging import getLogger

from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import current_user, login_user, logout_user, LoginManager
from werkzeug.exceptions import BadRequest, InternalServerError

from models import User, Post
from models.db import Session
from config import SECRET_KEY

app = Flask(__name__)
app.config.update(SECRET_KEY=SECRET_KEY)

login_manager = LoginManager()
login_manager.init_app(app)
logger = getLogger(__name__)


@login_manager.user_loader
def load_user(user_id):
    return Session.query(User).filter_by(id=user_id).one_or_none()


def validate_user_credentials(username: str, password: str):
    if not (
            username
            and len(username) >= 3
            and password
            and len(password) >= 5
    ):
        raise BadRequest("Username has to be at least 3 symbols and pass min 5")


def get_username_and_password_from_form(form: dict):
    username = form.get("username")
    password = form.get("password")
    validate_user_credentials(username, password)

    return username, password


def validate_username_unique(username):
    if Session.query(User).filter_by(username=username).one_or_none():
        raise BadRequest(f"User with username {username!r} already exists!")


@app.route("/sign_in.html", methods=("GET", "POST"))
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    if request.method == "GET":
        return render_template("sign_in.html")

    username, password = get_username_and_password_from_form(request.form)
    validate_username_unique(username)
    user = User(username, password)
    Session.add(user)

    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating user!")
        raise InternalServerError(f"Could not create new user! Error: {e}")
    login_user(user)
    return redirect(url_for("index"))


@app.route("/login.html", methods=("GET", "POST"))
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index.html"))
    if request.method == "GET":
        return render_template("login.html")
    username, password = get_username_and_password_from_form(request.form)
    user = Session.query(User).filter_by(username=username).one_or_none()
    if not user:
        return render_template("login.html", error_text="User not found")
    if user.password != User.hash_password(password):
        return render_template("login.html", error_text="Invalid username or password!")
    login_user(user)
    print("Uid:", user.id)
    return redirect(url_for("index"))


@app.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route('/')
@app.route('/index.html')
def index():
    posts = Session.query(Post).all()
    return render_template('index.html', posts=posts)


@app.route('/new_post.html', methods=("GET", "POST"))
def new_post():
    if not current_user.is_authenticated:
        return redirect(url_for("index.html"))
    if request.method == "GET":
        return render_template("new_post.html")
    form = request.form
    post_text = form['post_text']
    post = Post(post_text, current_user.id)
    Session.add(post)
    try:
        Session.commit()
    except Exception as e:
        logger.exception("Error creating post!")
        raise InternalServerError(f"Could not create new post! Error: {e}")
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run()

