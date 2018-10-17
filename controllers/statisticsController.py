from flask import render_template, redirect, request, url_for
import shlex
import subprocess
from app import app



@app.route("/statistics", methods=["GET", "POST"])
def statistics():

    command = "/usr/bin/Rscript /home/ceadd/Documentos/Deuana/Project/statistics_political_parties.R"
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
