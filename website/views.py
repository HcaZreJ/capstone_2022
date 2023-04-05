# This file contains the Python functions that will be run when a request is sent to the base
# page of the website.

# Flask & user account management import
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

# Miscellaneous imports
import json

# Blueprint declaration, so __init__.py can import everything below using register_blueprint()
views = Blueprint('views', __name__)
# You don't need to define this to have the same name as your file, but it just makes things easier

@views.route('/', methods=['GET', 'POST'])
# Within this above function, put whatever url / end point you want it to be
# A simple slash is put here, so this is the main page that one would go to when they
# simply type in the url of our website
def home():
    """Function that runs whenever a request is sent to the home page."""

    # Renders the home.html template, passing the current_user to it. You will be able
    # to access all info of the logged in user in the HTML, using {{ user.ATTRIBUTE }}
    return render_template("home.html", user=current_user)

###### Miscellaneous notes to make sure I will understand if I forget ######
# This file is a blueprint for our application,
# which means that it has a bunch of roots inside it (has a bunch of urls defined here)
# it's a kind of way to separate our app out, so we don't have to have all of our views 
# defined in one file, we can have them defined multiple files, split up and nicely organized
# ^^ That's what Blueprint() allows us to do