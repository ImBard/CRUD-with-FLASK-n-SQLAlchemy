from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models.user import Users

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def home():
  return render_template("index.html")


@app.route("/insert", methods=['POST'])
def insert():
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
  return redirect("/list")

@app.route("/list")
def list():
  users = Users.query.all()
  return render_template("users.html", users=users, len = len(users))

@app.route("/delete/<string:email>", methods=['POST'])
def delete(email):
  stmt = (
    delete(Users.email == email)
)
  return  redirect('/')


if __name__ == '__main__':
    app.run()