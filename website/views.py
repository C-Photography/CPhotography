#stores roots for website ie. home page, etc.
from flask import Blueprint, render_template#defined urls

views = Blueprint('views', __name__)

@views.route('/')#url to home endpoint try to put username here
def home():
    return render_template("home.html")

@views.route('/galleries')#url to events endpoint
def galleries():
    return render_template("galleries.html")

@views.route('/services')#url to Services Endpoint endpoint
def services():
    return render_template("services.html")

@views.route('/events')#url to events endpoint
def events():
    return render_template("events.html")

@views.route('/contact')#url to events endpoint
def contact():
    return render_template("contact.html")
