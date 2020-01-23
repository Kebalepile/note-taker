
from flask import (
    Blueprint, redirect,
    request, make_response,
    url_for, render_template,
    jsonify
)
from uuid import uuid4
# from noteapp.db import get_db
from noteapp.auth import login_required

bp = Blueprint("routes", __name__)


@bp.route("/")
def index():
    return redirect(url_for("routes.notes"))


@bp.route("/notes")
# @login_required
def notes():
    res = make_response(render_template("/home.html"))
    return res


@bp.route("/get_notes", methods=["GET"])
# @login_required
def get_all_notes():
    if request.method == "GET":
        pass
        # db = get_db()
        # notes = db.execute(
        #     'SELECT n.id, author_id, body, created'
        #     'FROM notes n JOIN users u on n.author_id = u.id'
        #     'ORDER BY created DESC'
        # ).fetachall()
       
        return make_response(jsonify({"notes":notes}, 200))


@bp.route("/create_note", methods=["POST"])
# @login_required
def create_note():
    if request.method == "POST":
        pass
        # data = request.json
        # db = get_db()
        # db.execute(
        #     'INSERT INTO notes (body, id) VALUES(?,?,?)',
        #     (data["body"], uuid4(), request.headers['d4rE'])
        # ).commit()
    return make_response(jsonify({"msg": "new note created."}), 201)


@bp.route("/delete", methods=["DELETE"])
# @login_required
def delete():
    if request.method == "DELETE":
        pass
        # data = request.json
        # db = get_db()
        # db.execute(
        #     "DELETE * FROM notes WHERE notes.id = ?",
        #     (data["id"])
        # ).commit()

    return make_response(jsonify({"msg": "note no more"}))
