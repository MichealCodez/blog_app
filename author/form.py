from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    first_name = StringField('First Name', [validators.Required()])
    last_name = StringField('Last Name', [validators.Required()])
    email = EmailField('Email', [validators.Required()])
    username = StringField('Username', [
        validators.Required(),
        validators.length(min=2, max=15)
    ])
    password = PasswordField('Password', [
        validators.Required(),
        validators.length(min=2, max=15)
        ])