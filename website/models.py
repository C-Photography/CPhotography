from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User_Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(1500))
    description = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Event_Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(1500))
    description = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    photos = db.relationship('Event_Photo')

class User(db.Model, UserMixin):
    #columns for the user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)#unique email of 150 characters
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    account_type = db.Column(db.String(150))#used to distinguish between user/administrator
    photos = db.relationship('User_Photo')
