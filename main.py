from website import create_app
# we can do the above, because the __init__.py file in the website folder made it into a python package
# Note: Whenever you put a __init__.py file into a folder, it becomes a python package
# by default, it will run all of the code in the __init__.py file, which means that we can import 
# anything that's defined in the __init__.py file

app = create_app()
# created the app using the create_app() function which uses Flask

if __name__ == '__main__':
    app.run(debug = True)
# The above two lines just says that only when we run the main.py file,
# (not when we import the file) are we going to run the app.
# We need this line because in situations when we just want to import the main.py file, it will run the web server.
# These two lines prevents it from happening

# app.run runs the Flask application, it will start off a web server.
# debug = True -> everytime we make a change to any of our python code, it going to automatically rerun the web server
# you would want to turn this off when you are in production, so that you can manually rerun the web server