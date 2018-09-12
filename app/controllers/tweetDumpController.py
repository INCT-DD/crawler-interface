from flask import render_template, redirect, request, url_for
import shlex
import subprocess
from app import app


@app.route("/tweetdump", methods=["GET", "POST"])
def tweetdump():

    command = "C:/Users/Deuana/Documents/R/R-3.5.1/bin/Rscript C:/Users/Deuana/Desktop/Project/candidates_timelines.R"
    args = shlex.split(command)

    try:
        p = subprocess.run(args, check=True)
        if p.returncode == 0:
            msg = "Coleta realizada com sucesso."
            return render_template("index.html", msg=msg)
        else:
            error = "Não foi possível realizar a consulta."
            return render_template("index.html", error=error)  

    except subprocess.CalledProcessError as error:
        error = "Não foi possível realizar a consulta."
        return render_template("index.html", error=error)  

    return render_template("index.html")
