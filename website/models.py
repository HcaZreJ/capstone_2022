# This is where we create database models. Objects created below are schemas / blueprints
# for what they must have, to ensure that the database is consistent across entries.

# Importing the database object from the __init__ of the current package
from . import db

# A custom class we can inherit that will give user objects specific things
# for a flask login
from flask_login import UserMixin

# func is a module in sql with some pre-defined easy-to-use functions
from sqlalchemy.sql import func

# Whenever you want to create a new database object, create a class here 
# that inherits from db.Model
class News(db.Model):
    """Inherited class that defines a blueprint for the News rating objects created in databse."""
    # Under this object, essentially we need to define all the "columns" we
    # want for this "table".

    id = db.Column(db.Integer, primary_key=True)
    # ^^ For all objects, it needs to have a primary_key column, which is a unique
    # identifier for each entry to ensure that we can find it even if it has duplicates
    # in other columns. Typically it will take on an Integer type.

    # Column for the id of the News article that the user rated, this links to the id
    # column of the data_v2.csv file in data_crawling_and_transformation folder. Set
    # unique=True so that user cannot rate a rated article again
    news_id = db.Column(db.Integer, unique=True)
    # ^^ Now I know this is not ideal, because if we changed the News Articles in the 
    # data_v2.csv file, this would all get messed up. But I searched for storing NumPy
    # arrays in sqlalchemy, and I could not find a very good method for storing such info.
    # Maybe something better will be implemented in the future, when I get better with 
    # sqlalchemy, and just databases in general.

    # Column for rating they gave to this News article
    rating = db.Column(db.Integer)

    # Forces all News ratings to be associated to a User.
    # Foreign Key = a column in database that always refers to a column of a different database
    # This user_id column will be an integer that must be a valid id of an existing user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # ^^ Seems like it is unreferenced due to the lower case, but sql needs foreign key declaration
    # to be in lower case, while Python class declarations need to be capitalized.

# For the user object, also inherit from UserMixin because we are using the flask_login
# module in our auth.py file to login users
class User(db.Model, UserMixin):
    """Inherited class that defines a blueprint for the User objects created in the database."""
    # Unique id
    id = db.Column(db.Integer, primary_key=True)

    # Email column, will be a String with a maximum length of 150. Cannot take on an existing email
    # when we specified the unique=True here
    email = db.Column(db.String(150), unique=True)

    # Password column, string as well with max length of 150
    password = db.Column(db.String(150))

    # First name column, string 150
    first_name = db.Column(db.String(150))

    # Column that stores all id of News rated by the user, we will be able to retrieve a user's
    # rated articles using this column. Capitalization is needed for a declaration of "relationship"
    news = db.relationship('News')