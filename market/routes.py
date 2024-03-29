from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from market import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
  purchase_form = PurchaseItemForm()
  selling_form = SellItemForm()
  # if purchase_form.validate_on_submit():
  #   print(request.form.get('purchased_item'))  #to display what item is purchased - in console
  if request.method == 'POST':
    #Purchase item logic
    purchased_item = request.form.get('purchased_item')
    p_item_object = Item.query.filter_by(name = purchased_item).first()
    if p_item_object:
      if current_user.can_purchase(p_item_object):
         p_item_object.buy(current_user)
         flash(f'Congratulations! You have purchased {p_item_object.name} for ₹{p_item_object.price}.', category = 'success')  
      else:
        balance = p_item_object.price - current_user.budget
        flash(f"Unfortunately, you lack ₹{balance} to purchase {p_item_object.name}", category = 'danger')
    
    #Sell item logic
    sold_item = request.form.get('sold_item')
    s_item_object = Item.query.filter_by(name = sold_item).first
    if s_item_object:
      if current_user.can_sell(s_item_object):
        s_item_object.sell(current_user)
        flash(f'Congratulations! You have sold {s_item_object.name} for ₹{s_item_object.price}.', category = 'success')
      else:
        flash(f'Oops..!! Something went wrong in selling  {s_item_object.name} .', category = 'danger')
    return redirect(url_for('market_page'))
        
  if request.method == 'GET':
    items = Item.query.filter_by(owner = None)
    owned_items = Item.query.filter_by(owner = current_user.id)
  return render_template('market.html', items=items, purchase_form = purchase_form, owner = current_user, owned_items =  owned_items, selling_form = selling_form) # changing owner to current user for check


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
    flash(f"Account created for {form.username.data}!, You are now logged in as {user_to_create.username}!", category = 'success')
    return redirect(url_for('market_page'))
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
      flash('Email and password incorrect! Please try again!',
            category='danger')

  return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
  logout_user()
  flash('You have been logged out!', category='info')
  return redirect(url_for("home_page"))

  
