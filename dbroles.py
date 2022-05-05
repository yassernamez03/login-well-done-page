from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(64), unique=True, index=True)
    users = db.relationship( 'User', backref='role', lazy=True)
    
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64))
    password=db.Column(db.String(64),nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
