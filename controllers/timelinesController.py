from flask import render_template, redirect, request, url_for
import shlex
import subprocess
from app import app

from app.models.timelineForm import timelineForm


@app.route("/timelines", methods=["GET", "POST"])
def timelines():

    form= timelineForm()

    if form.validate_on_submit():
        
        username = form.username.data

        if username:
            command = "/usr/bin/Rscript /home/ceadd/Documentos/Deuana/Project/candidates_timelines.R"
            args = shlex.split(command)
            args.append(username)
            
            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("timelines.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("timelines.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("timelines.html", form= form, error= error)

    return render_template("timelines.html", form= form)
