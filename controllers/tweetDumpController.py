from flask import render_template, redirect, request, url_for
import twint
from app import app
import shlex, subprocess
from app.scripts.tweetDump import tweetDump
from app.models.tweetDumpForm import tweetDumpForm

@app.route("/tweetdump", methods=["GET", "POST"])
def tweetdump():
    form= tweetDumpForm()
    
    if form.validate_on_submit():
      
        username = form.username.data
        output =  username + ".json"
        
        if username:
            command= "python /home/ceadd/Documentos/Deuana/Templates/Crawler/app/scripts/tweetDump.py"
            print(command)
            args = shlex.split(command)
            args.append(username)
            args.append(output)

            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("tweetdump.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("tweetdump.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("tweetdump.html", form= form, error= error)


    return render_template("tweetdump.html", form= form)