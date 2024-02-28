from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db, bcrypt
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market')
@login_required
def market_page():
  items = Item.query.all()
  return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    password_hash = bcrypt.generate_password_hash(
        form.password1.data.encode('utf-8'))
    user_to_create = User(username=form.username.data,
                          email_address=form.email_address.data,
                          password_hash=password_hash)
    db.session.add(user_to_create)
    db.session.commit()
    login_user(user_to_create)
    return redirect(url_for('login_page'))
  if form.errors != {}:  #If there are not errors from the validations
    for err_msg in form.errors.values():
      flash(f'Error: {err_msg[0]}', 'danger')
      print(f'Error: {err_msg[0]}')

  return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()

  if form.validate_on_submit() and request.method == "POST":
    attempted_user = User.query.filter_by(
        email_address=form.email.data).first()
    if attempted_user and bcrypt.check_password_hash(
        attempted_user.password_hash, form.password.data):

      login_user(attempted_user)
      flash(f'Success! You are logged in as {attempted_user.username}',
            category='success')
      return redirect(url_for('market_page'))
    else:
      flash('Username and password incorrect! Please try again!',
            category='danger')

  return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
  logout_user()
  flash('You have been logged out!', category='info')
  return redirect(url_for("home_page"))

  
