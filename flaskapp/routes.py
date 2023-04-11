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

@bp.route("/success/", methods=('GET', 'POST'))
def success():
    return render_template("routes/success.html")

@bp.route("/form/", methods=('GET', 'POST'))
def form():
    return render_template("routes/form.html")

@bp.route("/lesson/", methods=('GET', 'POST'))
def lesson():
    return render_template("routes/lesson.html")

@bp.route("/string/", methods=('GET', 'POST'))
def string():
    return render_template("routes/string.html")

@bp.route("/radius/", methods=('GET', 'POST'))
def radius():
    return render_template("routes/radius.html")

@bp.route("/payment/", methods=('GET', 'POST'))
def payment():
    return render_template("routes/payment.html")