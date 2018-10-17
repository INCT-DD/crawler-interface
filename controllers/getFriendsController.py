from flask import render_template, redirect, request, url_for
import shlex, subprocess
from app import app

from app.models.friendsForm import friendsForm

@app.route("/getfriends", methods=["GET", "POST"])
def getfriends():
    form = friendsForm()
    
    if form.validate_on_submit():
        
        username = form.username.data
               
        if username:
            
            command= "/usr/bin/Rscript /home/ceadd/Documentos/Deuana/Project/getFriends2.R"
            print(command)
            args = shlex.split(command)
            args.append(username)
            
            print(args)
            
            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("friends.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("friends.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("friends.html", form= form, error= error)

    return render_template("friends.html", form= form)