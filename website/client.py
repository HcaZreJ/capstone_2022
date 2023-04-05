# This page defines the Python functions that will be run, that renders 
# the webpages when the user is logged in

# Database & News object import
from .models import User, News
from . import db

# Flask & user account management import
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

# Import the recommendation functions from recommend.py
from .recommend import non_first_recommend, first_recommend

# Blueprint declaration, so __init__.py can import everything below using register_blueprint()
client = Blueprint('client', __name__)

# User's home page endpoint defined at /user-home, allows for GET & POST requests
@client.route('/user-home', methods=['GET', 'POST'])
@login_required # Specifies that a user must be logged in to access this page
def user_home():
    """Function that runs whenever a request is sent to the user's home page."""
    # If it is a POST request, meaning that the User just rated an article
    if request.method == 'POST':
        # Some functions to create a new database entry
        pass
    
    # Else it is a GET request, and we will be recommending 6 articles to the User
    else:
        # Sanity check to ensure that the user has already rated 6 articles, if not we need to redirect
        if len(current_user.news) < 6:
            # Flash a warning
            flash('You have not yet rated 6 articles, please rate again.', category="warning")
            # Redirect to first-time user page
            return redirect(url_for('client.first_time_user'))

        # Passed sanity check, generate recommendations as normal
        else:
            # Generate recommendations
            recommendations = non_first_recommend(current_user)

            # Render the user_home.html template, passing the current_user & recommendations to it.
            return render_template("user_home.html", user=current_user, recommendations=recommendations)

# First-time user's endpoint defined at / , allows for GET & POST requests
@client.route('/first-time', methods=['GET', 'POST'])
@login_required # Specifies that a user must be logged in to access this page
def first_time_user():
    """Function that runs whenever an account is created for the User and we need an initial capture of their preference."""
    # If it is a POST request, meaning that the user just rated an article
    if request.method == 'POST':
        # Some function to create a new database entry
        pass
    
    # Else it is a GET request, and we will be rendering the first 6 articles we need the user to rate
    else:
        # Sanity check to make sure that the user has not rated 6 articles yet
        if len(current_user.news) > 6:
            # Flash a waning
            flash("You have already rated 6 articles! Please do not attempt to reach this page.", category="warning")
            # Redirect to user home page
            return redirect(url_for('client.user_home'))
        
        # Passed sanity check, generate first 6 recommendations to get an initial capture
        else:
            # Generate recommendations
            recommendations = first_recommend()
            
            # Render the template with recommendations
            return render_template("first_time.html", user=current_user, recommendations=recommendations)