#auth stores login info
from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form #get posted data
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("signout.html")

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if len(email) < 4 or len(firstName) < 2 or password1 != password2 or len(password1) < 7:
            return render_template("signup.html", text="There was an error creating an account. Please try again.")
        else:
            return render_template("home.html", text="Account created successfully.")

