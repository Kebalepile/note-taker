import functools
import jwt
from datetime import datetime, timedelta
from flask import (
    Blueprint, redirect, url_for,
    request, make_response,
    render_template, g, session, jsonify,
    flash
)
from werkzeug.security import check_password_hash, generate_password_hash
from noteapp.db import get_db
from uuid import uuid4

bp = Blueprint("auth", __name__, url_prefix="/auth")



def login_required (view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.token is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return(wrapped_view)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.token = None
    else:
        token_id = jwt.decode(user_id,app.config["SECRET_KEY"])
        info = get_db(
            "SELECT * FROM users WHERE id = ?",
            (token_id["id"],)
        ).fetchone()
        g.token = jwt.encode({
            "user": info,
            "exp": datetime.utcnow() + timedelta(hours=72)
        },
        app.config["SECRECT_KEY"])

        
@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        print(request.form)
        email = request.form["email"]["email"]
        password = request.form["password"]
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE email = ?',
            (email,)
        ).fetchone()

        if user is None:
            error = "incorrect email"
        elif not check_password_hash(user["password"], password):
            error = "password incorrect"
        if error is None:
            session.clear()
            session.user_id = jwt.encode({
                "id": user["id"],
                "exp": datetime.utcnow() + timedelta(hours=72)
            }, app.config["SECRET_KEY"])
            return redirect("/")
        return flash(error) 
    return render_template("/login.html",login = True)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

@bp.route("/signup", methods=["POST", "GET"])
def sign_up():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm-password"]
        db = get_db()
        error = None

        if not email:
            error = "email required"
        elif not password:
            error = "password requried"
        elif password != confirm_password:
            error = "password does not match."
        elif db.execute('SELECT id FROM user WHERE email = ?', (email,)).fetchone() is not None:
            error = f'User {email} is already registered'
        if error is None:
            db.execute(
                "INSERT INTO users (id, email, password) VALUES(?,?,?)",
                (uuid4(),info["email"], generate_password_hash(info["password"]))
            ).commit()
            return redirect(url_for("auth.login", True))
        return flash(error)
    return render_template("/login.html", login = False)



# data = jwt.decode(token, app.config["SECRET_KEY"])
# token = jwt.encode({
#'user': user,
#'exp':  datatime.datatime.utcnow() + datatime.timedelta(hours=72) 
# },
# app.config['SECRET_KEY'])
