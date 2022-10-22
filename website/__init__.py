from flask import Flask

def create_app():
    app = Flask(__name__)

    # The above three lines is just how you initialize Flask

    app.config['SECRET_KEY'] = 'adfadvc aafqfgtmflkdiqo qojfqrtkmn'
    # ^ encrypt or secure the cookies and session data related to our website,
    # just type a random string and assign to the variable
    # in production, never share this secret key with anyone

    from .views import views
    # imports the variable of views from the views.py file
    from .auth import auth
    # imports the variable of auth from the auth.py file

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')
    # The above two lines registered the blueprints from these two variables into our flask application
    # the url_prefix says that all of the urls that are stored inside of these blueprint files
    # will need to accessed by an url thats adds whatever's inside of it as a prefix
    # e.g. if we put '/main/' in the prefix, then all routes in eg. views will need to be accessed by
    # server_address/main/route.


    return app