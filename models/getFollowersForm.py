from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class getFollowersForm(FlaskForm):
    profile = StringField("profile", validators= [DataRequired()])
    followers = IntegerField("followers", validators= [DataRequired()])
    