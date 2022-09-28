from flask_sqlalchemy import SQLAlchemy
from db import db

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String, nullable=False)
  age = db.Column(db.String, nullable=False)
  email = db.Column(db.String, unique=True)