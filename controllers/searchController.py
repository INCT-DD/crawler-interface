from flask import render_template, redirect, request, url_for
import twint
from app import app
import shlex, subprocess
from app.scripts.searchTwint import searchTwint
from app.models.searchForm import searchForm

@app.route("/search", methods=["GET", "POST"])
def search():
    form= searchForm()
    
    if form.validate_on_submit():
      
        trackKeyword = form.trackKeyword.data
        initialDate = str(form.initialDate.data)
        finalDate = str(form.finalDate.data)
        dbCollection = form.dbCollection.data
        #output =  trackKeyword + ".json"

        print(initialDate, finalDate)

        if trackKeyword and initialDate and finalDate and dbCollection:
            command= "python /home/ceadd/Documentos/Deuana/Templates/Crawler/app/scripts/searchTwint.py"
            print(command)
            args = shlex.split(command)
            args.append(trackKeyword)
            #args.append(output)
            args.append(initialDate)
            args.append(finalDate)
            args.append(dbCollection)
            
            try:
                p = subprocess.run(args, check=True)
                if p.returncode == 0:
                    msg= "Coleta realizada com sucesso."
                    return render_template("search.html", form= form, msg= msg)

            except subprocess.CalledProcessError as error:
               error= "Não foi possível realizar a consulta."
               return render_template("search.html", form= form, error= error)
             
        else:
            error= "Dados inválidos. Insira novamente por favor."
            return render_template("search.html", form= form, error= error)


    return render_template("search.html", form= form)