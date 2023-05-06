import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()

#User database
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    username = db.Column(db.String(32),unique=True,nullable=False)
    email = db.Column(db.String(64), unique=True,nullable=False)
    password = db.Column(db.String(32),nullable=False)
    

# #Deck database
class Deck(db.Model):
    __tablename__ = 'decks'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(255),nullable=False)
    last_reviewed = db.Column(db.DateTime,nullable=False,default=datetime.now())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    score = db.Column(db.Integer,default=0)
    cards = db.relationship('Card', backref='decks', lazy=True,cascade='all, delete')

class Card(db.Model):

    __tablename__ = 'cards'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    front = db.Column(db.String(255),nullable=False)
    back = db.Column(db.String(255),nullable=False)
    deck_id = db.Column(db.Integer,db.ForeignKey("decks.id",ondelete='CASCADE'),nullable=False)
    
    def serialize(self):
        return json.dumps(self, default=lambda o: o.__dict__)
    
    

