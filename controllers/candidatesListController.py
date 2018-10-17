from flask import render_template, redirect, request, url_for
from app import app, mongo

@app.route("/candidateslist", methods=["GET", "POST"])
def candidateslist():
     
     if request.method == 'GET':
        data = mongo.db.candidates.find()
        print(data)
        return render_template("candidateslist.html", data = data)
