from flask_wtf import FlaskForm
from wtforms import StringField, DateField 
from wtforms.validators import DataRequired

class searchForm(FlaskForm):
    trackKeyword = StringField("trackKeyword", validators= [DataRequired()])
    initialDate = DateField("initialDate",format= "%Y-%m-%d", validators= [DataRequired()])
    finalDate = DateField("finalDate", format= "%Y-%m-%d", validators= [DataRequired()])
    dbCollection = StringField("dbCollection", validators= [DataRequired()])
