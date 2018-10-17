from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class getRepliesForm(FlaskForm):
    profile = StringField("profile", validators= [DataRequired()])
    numberTweets = IntegerField("numberTweets", validators= [DataRequired()])
    