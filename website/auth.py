from flask import Blueprint

auth = Blueprint('auth', __name__)


# A page for logging into user accounts
@auth.route('/login')
def login():
    return '<p>Login</p>'

# A page for logging out of user accounts
@auth.route('/logout')
def logout():
    return '<p>Logout</p>'

# A page for sign up for an account
@auth.route('/sign-up')
def sign_up():
    return '<p>Sign Up</p>'