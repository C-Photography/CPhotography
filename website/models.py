from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    description = db.Column(db.String(15000))
    gallery_collections = db.relationship('Gallery_Collection')
class Gallery_Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100))
    data = db.Column(db.LargeBinary)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    description = db.Column(db.String(15000))
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallery.id'))

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    description = db.Column(db.String(15000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_collections = db.relationship('User_Collection')
class User_Collection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(1500))
    description = db.Column(db.String(15000))
    data = db.Column(db.LargeBinary)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))

class Event_Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo_name = db.Column(db.String(1500))
    description = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(15000))
    post_date = db.Column(db.DateTime(timezone=True), default=func.now())
    start_date = db.Column(db.DateTime(timezone=True), default=func.now())
    end_date = db.Column(db.DateTime(timezone=True), default=func.now())
    photos = db.relationship('Event_Photo')

class User(db.Model, UserMixin):
    #columns for the user
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)#unique email of 150 characters
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    account_type = db.Column(db.String(150))#used to distinguish between user/administrator
    portfolios = db.relationship('Portfolio')