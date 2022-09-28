from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from routes import crud
from db import db


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/crud"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(crud)

if __name__ == "__main__": 
  app.run()