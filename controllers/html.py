from http.client import OK

from flask import render_template

from config.config import app


@app.route("/login")
def login_page():
    return render_template('a.html'), OK
