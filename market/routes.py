from wtforms.fields.simple import PasswordField
from market import app
from flask import render_template
from market.models import Item, User
from market.forms import RegisterForm
from market import db

@app.route('/')  
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():
  items = Item.query.all()
  return render_template('market.html', items=items)

@app.route('/register')
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    user_to_create = User(username=form.username.data, email_address=form.email_address.data, password = form.password1.data)
    
    return render_template('register.html', form=form)

