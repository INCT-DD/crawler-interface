from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class timelineForm(FlaskForm):
    username = StringField("username", validators= [DataRequired()])
    