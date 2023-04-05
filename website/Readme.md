# Website

This is the main folder for the project that contains the heart of the web app's code.

The sections are as follows:

 - `templates`: Folder that contains the HTML templates, which gets rendered along with some information, when a request is sent to specific endpoints.
     - `base.html`: The very base HTML template of all other HTML templates.
     - `first_time.html`: The HTML template for a newly signed-up user, requests user to rate 6 articles so we can have an initial capture of their preference. Can only be accessed when logged in and the user has not already rated 6 articles.
     - `home.html`: The HTML template for the home page of the website. Can only be accessed when not logged in.
     - `login.html`: The HTML template for the login page. Can only be accessed when not logged in.
     - `sign_up.html`: The HTML template for the sign up page. Can only be accessed when not logged in.
     - `user_home.html`: The HTML template for the home page of a logged-in user. Shows 6 recommendations to the user, given the captured preference. Can only be accessed when logged in and the user has already rated more than 6 articles.
 - `__init__.py`: The Python script that sets up the app. Defines the `create_app()` function which gets called by the `main.py` script in the outer folder.
 - `auth.py`: The Python script that handles the authentication endpoints. Deals with requests sent to `/login`, `/logout`, and `sign-up`.
 - `client.py`: The Python script that handles a logged-in user's endpoints. Deals with requests sent to `/user-home` and `/first-time`.
 - `models.py`: The Python script that defines the objects in the sqlite database. Defined a `User` object and a `News` object. The relationship of `News` to `User` is many to one. `News` represents all the news that the user read, along with the rating the user gave.
 - `recommend.py`: The Python script that defined two recommendation functions for non-first-time and first-time users. Uses the sqlite database and data from the web crawling folder.
 - `views.py`: The Python script that handles the home page endpoint. Deals with requests sent to `/`.