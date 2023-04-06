# This page defines the Python functions that will be run, that renders 
# the webpages when the user is logged in

# Database & News object import
from .models import User, News
from . import db

# Flask & user account management import
from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
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
    # Declare a global variable for recommendations, because we will need to refer to it later in 'POST'
    # requests to check whether the user has rated all 6 articles or not, and make sure that they
    # don't change.
    global recommendations

    # If it is a POST request, meaning that the User just rated an article
    if request.method == 'POST':
        # Record form data
        newsId = int(request.form.get('newsId'))
        rating = int(request.form.get('rating'))
        position = int(request.form.get('position'))

        # Create a new entry for the database & commit to the change
        rated_news = News(news_id=newsId, rating=rating, user_id=current_user.id)
        db.session.add(rated_news)
        db.session.commit()

        # Generate a new recommendation
        new_recommend = non_first_recommend(current_user, x=1)

        # Delete the rated article from the list, add the new article in
        del recommendations[position]
        recommendations.append(new_recommend)

        # Render the home page again, along with a flashed message
        flash("Thank you for your rating.", category="success")
        return render_template("user_home.html", user=current_user, recommendations=recommendations,
                               iterator=[i for i in range(6)])
    
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
            return render_template("user_home.html", user=current_user, recommendations=recommendations,
                                   iterator=[i for i in range(6)])

# First-time user's endpoint defined at / , allows for GET & POST requests
@client.route('/first-time', methods=['GET', 'POST'])
@login_required # Specifies that a user must be logged in to access this page
def first_time_user():
    """Function that runs whenever an account is created for the User and we need an initial capture of their preference."""
    # Declare a global variable for recommendations
    global first_recommendations

    # If it is a POST request, meaning that the user just rated an article
    if request.method == 'POST':
        # Retrieve data from the form
        ratings = []
        for i in range(6):
            rating = request.form.get('rating'+str(i))
            ratings.append(int(rating))

        # Create new entries in the database for the user
        for j in range(6):
            rated_news = News(news_id=int(first_recommendations[j].name), rating=ratings[j], user_id=current_user.id)
            db.session.add(rated_news)
        db.session.commit()

        # Flash a successful message
        flash("Thank you for rating, we have an initial capture of your preference.", category="success")

        # Redirect the user to the client home page
        return redirect(url_for('client.user_home'))
    
    # Else it is a GET request, and we will be rendering the first 6 articles we need the user to rate
    else:
        # Sanity check to make sure that the user has not rated 6 articles yet
        if len(current_user.news) >= 6:
            # Flash a waning
            flash("You have already rated 6 articles! Please do not attempt to reach this page.", category="warning")
            # Redirect to user home page
            return redirect(url_for('client.user_home'))
        
        # Passed sanity check, generate first 6 recommendations to get an initial capture
        else:
            # Generate recommendations
            first_recommendations = first_recommend()
            
            # Render the template with recommendations
            return render_template("first_time.html", user=current_user, recommendations=first_recommendations,
                                   iterator=[i for i in range(6)])