from flask_wtf import FlaskForm
from wtforms import StringField

class RegisterForm(FlaskForm):
  username = StringField(label = 'username')
  email_address = StringField(label = 'email')
  