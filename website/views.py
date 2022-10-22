from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


# We are going to define this file as a blueprint for our application
# which means that it has a bunch of roots inside it (has a bunch of urls defined here)
# it's a kind of way to separate our app out, so we don't have to have all of our views 
# defined in one file, we can have them defined multiple files, split up and nicely organized
# ^^ That's what blueprint allows us to do

views = Blueprint('views', __name__)
# You don't need to define this to have the same name as your file, but it just makes things
# easier, it keeps things really simple

## ^^ This above same thing will be done in auth and won't be explained further

@views.route('/', methods=['GET', 'POST'])
## Within this above function, put whatever url / end point you want it to be
# A simple slash is put here, so this is the main page that one would go to when they
# simply type in the url of our website
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)
# This defined function here home() will run, whenever we go to the above specified route

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})