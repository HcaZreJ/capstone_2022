# This file defines the Python functions that will be run when a request is sent
# to the login, logout, and sign-up pages. Basically when it is a GET request,
# we simply render the web page, and when it is a POST request, we handle user login/logout.

# Flask imports
from flask import Blueprint, render_template, request, flash, redirect, url_for

# User account management with database, User object, and flask_login functions
from . import db
from .models import User
from flask_login import login_user, login_required, logout_user, current_user

# Password hashing
from werkzeug.security import generate_password_hash, check_password_hash

# Email verification
import re

# Blueprint declaration, so __init__.py can import everything below using register_blueprint()
auth = Blueprint('auth', __name__)

# A page for logging into user accounts
@auth.route('/login', methods=['GET', 'POST'])
# HTTP is the protocol that we use to transfer info between server & client. There are many different type of requests
# possible from a client, to differentiate the actions they are attempting so that the server could react accordingly.
# GET is usually just for retrieving the webpage, while POST is usually making a change to the database / state of the website.
# Use methods=[] to specify the name of the requests that this page can handle, by default there's only 'GET'.
def login():
    """Function that runs when a request is sent to the /login page."""
    # This request variable (which was imported at the top) contains information of the request whenever
    # it is accessed inside of a route, such as URL, method, etc. In our case, the information are all stored under
    # the 'form' attribute, as you can see in the login.html template.
    if request.method == 'POST':
        # Get email & password fields to login the user
        email = request.form.get('email')
        password = request.form.get('password')

        # Look for all entries of 'User', with column email == email value from above,
        # then get the first one of them
        user = User.query.filter_by(email=email).first()

        # If user exists
        if user:
            # If password hash matches (by hashing the second argument and compare with first)
            if check_password_hash(user.password, password):
                # "flash" is a function built-in by Flask that allows you to flash some message to the user on that page,
                # the category help you differentiate so you can show messages in different colors.
                flash('Logged in successfully!', category='success')

                # Logins the user, Flask remembers this unless session closed
                login_user(user, remember=True)

                # Sanity check to ensure that user has already rated 6 articles, or else we cannot give 
                # meaningful recommendations
                if len(user.news) < 6:
                    # Flash a warning
                    flash('You have not yet rated 6 articles, please rate again.', category="warning")
                    # Redirect to first-time user page
                    return redirect(url_for('client.first_time_user'))

                else:
                    # Redirect the user to the client home page when they signed in successfully
                    return redirect(url_for('client.user_home'))
            
            # Else password hash did not match, flash an error message
            else:
                flash('Incorrect password, try again.', category='error')
        
        # Else user does not exist, flash an error
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)
    # ^^ What this render_template does is that it renders login.html, while passing the current_user object to the template
    # under the name of 'user', so that you can access data ob this object by calling {{ user.whatever }} in the templates
    # with Jinga

# A page for logging out of user accounts
@auth.route('/logout')
@login_required
# ^^ This ensures that this page is only accessible when a user is logged in
def logout():
    """Function that runs when a request is sent to the /logout page."""
    # Logouts the current user
    logout_user()

    # Redirects to the Home page
    return redirect(url_for('views.home'))


# A page for sign up for an account that allows GET & POST requests
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """Function that runs when a request is sent to the /sign-up page."""
    # If it was a POST request
    if request.method == 'POST':
        # Obtain all info entered in the form
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Sanity check for whether the email exists or not
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        
        # Sanity checks on the info entered in the form
        elif re.match("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$", email) != True:
            flash('You must enter a valid email.', category='error')
        elif len(first_name) < 1:
            flash('You must enter a first name.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')

        # Else passed sanity check, we create a user account for the user
        else:
            # Create a new user object, filling the fields with info from POST request
            # The password hash ensures that there is no way to tell the original password,
            # one may only check if password correct by verifying the hashes
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # Add the new user object to the database
            db.session.add(new_user)
            # Commit to this change in the database
            db.session.commit()

            # Logins the user, Flask remembers this unless session closed
            login_user(new_user, remember=True)
            # Flash a success message
            flash('Account created!', category='success')

            # Redirect a signed up user to the first-time-user page, to get an initial capture of their preference
            return redirect(url_for('client.first_time_user'))

    # GET requests go straight to rendering the sign_up.html template, note the user 
    # specification here is still needed because we used it in the base template
    return render_template("sign_up.html", user=current_user)