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
            command= "C:/Users/Deuana/Documents/R/R-3.5.1/bin/Rscript C:/Users/Deuana/Desktop/Project/tweet_stream_rtweet.R"
            args = shlex.split(command)
            args.append(trackKeyword)
            args.append(trackTimeout)
            args.append(dbCollection)
            
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