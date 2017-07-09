from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    stringurl = StringField('stringurl',
                            [validators.InputRequired()],
                            render_kw={"placeholder": 
                            "http://dayviews.com/user/id_of_first_image/"})
    email = StringField('email',
                        [validators.Email("Please enter your email address.")])
    username = StringField('username')
    password = PasswordField('password')
    save_text = BooleanField('save_text', default=True)
