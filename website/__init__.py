# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# User account management import
from flask_login import LoginManager

# System path module import for database verification
from os import path

# Creating a database with flask's sqlalchemy
db = SQLAlchemy()
# Name for the database
DB_NAME = "database.db"

def create_app():
    '''
    The central function that creates a Flask app, sets up the database, registers HTML
    blueprints, and sets up the server to handle HTML requests.
    '''
    app = Flask(__name__)
    # Initialize a Flask app

    app.config['SECRET_KEY'] = 'adfadvc aafqfgtmflkdiqo qojfqrtkmn'
    # ^ encrypt or secure the cookies and session data related to our website,
    # just type a random string and assign to the variable
    # in production, never share this secret key with anyone
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # ^^ Telling Flask that we will be using this sq lite database we created at the top,
    # with name equal to DB_NAME. Data will be stored in the 'website' folder.

    db.init_app(app)
    # ^^ Initialize our database, by telling it this is the app that we will be using
    # for this database

    from .views import views
    # Imports the 'views' blueprint from the views.py file
    from .auth import auth
    # Imports the 'auth' blueprint from the auth.py file
    from .client import client
    # Imports the 'client' blueprint from the client.py file

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(client, url_prefix='/')
    # The above three lines registered the blueprints from these three variables into our flask application
    # the url_prefix says that all of the urls that are stored inside of these blueprint files
    # will need to accessed by an url thats adds whatever's inside of it as a prefix
    # e.g. if we put '/main/' in the prefix, then all routes in eg. views will need to be accessed by
    # server_address/main/route.

    from .models import User, News
    # Imports the two sql classes from the models.py file
    # We just need this to ensure that the two classes are defined before we create the database

    # Checks if there is a database, creates one if there is not
    create_database(app)

    # LoginManager object initialization, to handle the session's user signup, login, logout
    login_manager = LoginManager()
    # Where to direct when no user is logged in
    login_manager.login_view = 'auth.login'
    # Specify which app we are using
    login_manager.init_app(app)

    # Tells Flask to use the function below to load a user
    @login_manager.user_loader
    def load_user(id):
        """Searches the database for the user id, returns the User object if found."""
        # Searches the database for the user, difference from filter_by is that it searches through the primary_key by deafult
        return User.query.get(int(id))

    return app


def create_database(app):
    """Creates a database if there is not one in the website folder."""
    # If the database does not exist in path
    if not path.exists('website/' + DB_NAME):
        # Create database with the Flask app's context, it knows where the 
        # database is from line 24's database URI
        with app.app_context():
            db.create_all()
        # Debug message
        print('Created Database!')