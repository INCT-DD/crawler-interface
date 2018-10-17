from flask import render_template, redirect, request, url_for
import shlex, subprocess
from app import app

from app.models.streamForm import streamForm

@app.route("/stream", methods=["GET", "POST"])
def stream():
    form = streamForm()
    
    if form.validate_on_submit():
        
        trackKeyword = form.trackKeyword.data
        trackTimeout = form.trackTimeout.data
        dbCollection = form.dbCollection.data
        
        if trackKeyword and trackTimeout and dbCollection: 
            #print(trackKeyword, trackTimeout, dbCollection)
            command= "/usr/bin/Rscript /home/ceadd/Documentos/Deuana/Project/tweet_stream_rtweet.R"
            print(command)
            args = shlex.split(command)
            args.append(trackKeyword)
            args.append(trackTimeout)
            args.append(dbCollection)
            print(args)
            
            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("streamForm.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("streamForm.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("streamForm.html", form= form, error= error)

    return render_template("streamForm.html", form= form)