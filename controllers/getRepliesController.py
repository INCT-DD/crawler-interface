from flask import render_template, redirect, request, url_for, abort, jsonify, send_from_directory, make_response, send_file 
import twint
import os
from app import app
import shlex, subprocess
from app.scripts.getReplies import getReplies
from app.models.getRepliesForm import getRepliesForm
from config import UPLOAD_FOLDER


@app.route("/getreplies", methods=["GET", "POST"])
def getreplies():
    form= getRepliesForm()
    
    if form.validate_on_submit():
      
        profile = form.profile.data
        numberTweets =  str(form.numberTweets.data)
        
        if profile and numberTweets:
            command= "python /home/ceadd/Documentos/Deuana/Templates/Crawler/app/scripts/getReplies.py"
            print(command)
            args = shlex.split(command)
            args.append(profile)
            args.append(numberTweets)

            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("getreplies.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("getreplies.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("getreplies.html", form= form, error= error)


    return render_template("getreplies.html", form= form)

@app.route('/download', methods=["GET", "POST"])
def download():  
    filename = "result.csv"
    path = os.path.join(UPLOAD_FOLDER, filename)

    try:
	    return send_file(path, as_attachment=True)
    except Exception as e:  
        return str(e)
   
    