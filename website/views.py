#stores roots for website ie. home page, etc.
from flask import Blueprint, render_template#defined urls
from flask_login import login_required, current_user
#from . import db
views = Blueprint('views', __name__)

#non user home
@views.route('/')#url to home endpoint try to put username here
def home():
    return render_template("home.html", user=current_user)

@views.route('/portfolio')#url to events endpoint
@login_required
def portfolio():
    return render_template("portfolio.html", user=current_user)

@views.route('/services')#url to Services Endpoint endpoint
def services():
    return render_template("services.html", user=current_user)

@views.route('/events')#url to events endpoint
def events():
    return render_template("events.html", user=current_user)

@views.route('/contact')#url to events endpoint
def contact():
    return render_template("contact.html", user=current_user)

#user home (considering implementation)
#@views.route('/home')
#@login_required