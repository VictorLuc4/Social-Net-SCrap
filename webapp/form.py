from flask_wtf import FlaskForm
from wtforms import StringField, validators, RadioField, IntegerField, DecimalField
from wtforms.validators import NumberRange


class searchform(FlaskForm):
    search = StringField('Search', [validators.Length(min=0, max=50), validators.DataRequired()])


class scrapform(FlaskForm):
    radio = RadioField('radio', choices=[('user','Username'),('hashtag','Hashtag')], default='user')
    data = StringField('data', [validators.Length(min=0, max=100), validators.DataRequired()])
    number = IntegerField('number', validators=[
                validators.Required(),
                validators.NumberRange(min=1, max=20)
            ])
