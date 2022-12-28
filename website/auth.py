#auth stores login info
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
auth = Blueprint('auth', __name__)
from flask_login import login_user, login_required, logout_user, current_user

@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method== 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()#return first result
        if user: #if value returned
            if check_password_hash(user.password, password):
                login_user(user, remember=True)#login user, remember login information
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Login attempt failed. Incorrect password.', category='error')
        else:
            flash('Login attempt failed. Email not found.')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        account_type = 'standard'
        user = User.query.filter_by(email=email).first()#check if user already exists
        if len(email) < 4 or len(first_name) < 2 or password1 != password2 or len(password1) < 7 or user:
            flash('There was an error creating an account. Please try again.', category='error')
        else:
            new_user= User(email=email, first_name=first_name, last_name=last_name, account_type=account_type, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created', category='success')
            return redirect(url_for('views.home'))
    return render_template("signup.html", user=current_user)

