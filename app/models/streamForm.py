from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, TextAreaField, RadioField
from wtforms.validators import DataRequired, regexp

class streamForm(FlaskForm):
    trackKeyword = StringField("trackKeyword", validators= [DataRequired()])
    trackTimeout = StringField("trackTimeout", validators= [DataRequired()])
    dbCollection = StringField("dbCollection", validators= [DataRequired()])


