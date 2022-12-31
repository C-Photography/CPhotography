#stores roots for website ie. home page, etc.
from flask import Blueprint, render_template, request, redirect, flash, url_for#defined urls
from flask import current_app as app
from flask_login import login_required, current_user
#from . import db
import os
from . import __init__
from werkzeug.utils import secure_filename
views = Blueprint('views', __name__)

def allowed_image(filename):
        if not '.' in filename:
            return False
        ext = filename.rsplit('.',1)[1]
        if ext.upper() in app.config['ALLOWED_IMAGE_ETENSTIONS']:
            return True
        else:
            return False

#non user home
@views.route('/', methods=["GET", "POST"])#url to home endpoint try to put username here
def home():
    if request.method == "POST":
        if request.files:#post admin image uploads still need collection to post to
            image = request.files["image"]
            if image.filename == "":
                flash('Image must have a file name!', category='error')
                return redirect(url_for('views.home'))
            if not allowed_image(image.filename):
                flash('Image is not the correct file type', category='error')
                return redirect(url_for('views.home'))
            else:
                filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))
        #post new collection
    
    if current_user.is_authenticated: #get user info
        user = current_user
    else:
        user = 'Guest'
    return render_template("home.html", user=user)

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