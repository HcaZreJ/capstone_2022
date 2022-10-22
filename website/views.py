from flask import Blueprint

# We are going to define this file as a blueprint for our application
# which means that it has a bunch of roots inside it (has a bunch of urls defined here)
# it's a kind of way to separate our app out, so we don't have to have all of our views 
# defined in one file, we can have them defined multiple files, split up and nicely organized
# ^^ That's what blueprint allows us to do

views = Blueprint('views', __name__)
# You don't need to define this to have the same name as your file, but it just makes things
# easier, it keeps things really simple

## ^^ This above same thing will be done in auth and won't be explained further

@views.route('/')
## Within this above function, put whatever url / end point you want it to be
# A simple slash is put here, so this is the main page that one would go to when they
# simply type in the url of our website
def home():
    return '<h1>Test</h1>'
    # renders Test on the website with simple html tags
# This defined function here home() will run, whenever we go to the above specified route