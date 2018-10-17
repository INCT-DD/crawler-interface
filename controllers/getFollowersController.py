from flask import render_template, redirect, request, url_for
import twint
from app import app
import shlex, subprocess
from app.models.getFollowersForm import getFollowersForm

@app.route("/getfollowers", methods=["GET", "POST"])
def getfollowers():
    form= getFollowersForm()
    
    if form.validate_on_submit():
      
        profile  = form.profile.data
        followers = str(form.followers.data)
        dbCollection = profile + "Collection"
        
        
        if profile and followers:
            command= "/usr/bin/Rscript /home/ceadd/Documentos/Deuana/Templates/Crawler/app/scripts/get_followers.R"
            args = shlex.split(command)
            args.append(profile)
            args.append(followers)
            args.append(dbCollection)

            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("getfollowers.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("getfollowers.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("getfollowers.html", form= form, error= error)


    return render_template("getfollowers.html", form= form)