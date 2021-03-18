from flask_wtf import FlaskForm
from wtforms import StringField, validators

class searchform(FlaskForm):
    search = StringField('Search', [validators.Length(min=0, max=50), validators.DataRequired()])