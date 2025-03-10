from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from .book_api import search_books  # Ensure this import is correct

views = Blueprint('views', __name__)

@views.route('/search-books', methods=['GET'])
def search_books_route():
    query = request.args.get('query')
    books = search_books(query)
    return jsonify(books)

@views.route('/', methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = request.form.get('note')
        book_title = request.form.get('book_title')

        if len(note) < 1:
            flash("no note added")
            #flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id, book_title=book_title)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=["POST"])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
