from datetime import datetime
from email.policy import default
from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80),unique=True,nullable=False)
    email = db.Column(db.String(100),unique=True,nullable=False)
    password = db.Column(db.Text(),nullable=False)
    created_at = db.Column(db.Datetime,default=datetime.now())
    updated_at = db.Column(db.Datetime,onupdate=datetime.now())
    bookmarks = db.relationship('Bookmark',backref="user")
    
    
    
    def __repr__(self) -> str:
        return 'User>>> {self.username}'
    
class Bookmark(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text(),nullable=True)
    url = db.Column(db.Text(),nullable=False)
    short_url = db.Column(db.String(3),nullable=False)
    visits = id = db.Column(db.Integer, default=0)
    user_id = id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.Datetime,default=datetime.now())
    updated_at = db.Column(db.Datetime,onupdate=datetime.now())
    
    def __repr__(self) -> str:
        return 'Bookmark>>> {self.url}'
    
    def __init__(self, **kwargs) :
        super().__init__(**kwargs)