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
