import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskapp.db import get_db

bp = Blueprint('routes', __name__) # , url_prefix='/routes'

@bp.route("/", methods=('GET', 'POST'))
def home():
    return render_template("routes/home.html")

@bp.route("/thanks/", methods=('GET', 'POST'))
def thanks():
    return render_template("routes/thanks.html")

@bp.route("/schedule/", methods=('GET', 'POST'))
def schedule():
    return render_template("routes/schedule.html")

@bp.route("/lesson/", methods=('GET', 'POST'))
def lesson():
    return render_template("routes/lesson.html")

@bp.route("/string/", methods=('GET', 'POST'))
def string():
    return render_template("routes/string.html")

@bp.route("/radius/", methods=('GET', 'POST'))
def radius():
    return render_template("routes/radius.html")

@bp.route("/contact/", methods=('GET', 'POST'))
def contact():
    return render_template("routes/contact.html")

@bp.route("/twine/", methods=('GET', 'POST'))
def twine():
    return render_template("routes/twine.html")

@bp.route("/summary/", methods=('GET', 'POST'))
def summary():
    return render_template("routes/summary.html")