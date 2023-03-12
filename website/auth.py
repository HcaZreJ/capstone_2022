from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# A page for logging into user accounts
@auth.route('/login', methods=['GET', 'POST'])
# HTTP is the protocol that we use to transfer info between server & client. There are many different type of requests
# possible from a client, to differentiate the actions they are attempting so that the server could react accordingly.
# GET is usually just for retrieving the webpage, while POST is usually making a change to the database / state of the website.
# Use methods=[] to specify the name of the requests that this page can handle, by default there's only 'GET'.
def login():
    # This request variable (which was imported at the top) contains information of the request whenever
    # it is accessed inside of a route, such as URL, method, etc. In our case, the information are all stored under
    # the 'form' attribute, as you can see in the login.html template.
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                # "flash" is a function built-in by Flask that allows you to flash some message to the user on that page,
                # the category help you differentiate so you can show messages in different colors.
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)
    # what this render_template does is that it renders login.html, while passing the current_user object to the template
    # under the name of 'user', so that you can access data ob this object by calling {{ user.whatever }} in the templates
    # with Jinga

# A page for logging out of user accounts
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# A page for sign up for an account that allows GET & POST requests
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # If it was a POST request
    if request.method == 'POST':
        # Obtain all info entered in the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        
        # Sanity checks on the info entered in the form
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)