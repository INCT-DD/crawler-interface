from flask import render_template, redirect, request, url_for
from app import app


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")