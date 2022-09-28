from flask import Blueprint, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from models.user import Users
from db import db

crud = Blueprint("routes", __name__)


@crud.route("/")
def home():
    return render_template("index.html")


@crud.route("/create", methods=['POST'])
def create():
    nome = request.form.get('name')
    age = request.form.get('age')
    email = request.form.get('email')

    usuario = Users(
        nome=nome,
        age=age,
        email=email
    )
    db.session.add(usuario)
    db.session.commit()
    db.session.close()

    return redirect(url_for("routes.list"))


@crud.route("/list")
def list():
    users = Users.query.all()
    return render_template("users.html", users=users, len=len(users))


@crud.route("/delete/<email>", methods=['GET', 'POST'])
def delete(email):
    data = Users.query.filter(Users.email == email).first()
    db.session.delete(data)
    db.session.commit()
    return redirect(url_for("routes.list"))


@crud.route("/update/<email>", methods=["POST", "GET"])
def update(email):
    user = Users.query.filter(Users.email == email).first()

    user.nome = request.form.get('name')
    user.age = request.form.get('age')
    user.email = request.form.get('email')

    db.session.commit()

    return redirect(url_for("routes.list"))
