from market import app, db_session
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():

  items = Item.query.all()
  return render_template('market.html', items=items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()

  if form.validate_on_submit():
    user_to_create = User(form.username.data, form.email_address.data, form.password1.data)
    db_session.add(user_to_create)
    db_session.commit()
    return redirect(url_for('market_page'))
   
  if form.errors != {}: #if there are errors from the validations
    for err_msg in form.errors.values():
      flash(f'{err_msg[0]}', category='danger')
  return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()

  if form.validate_on_submit():
    attempted_user = User.query.filter_by(username=form.username.data).first()

    if attempted_user and attempted_user.check_password_correction(
      attempted_password=form.password.data
    ):
      login_user(attempted_user)
      flash(f'Success: You are logged in as: {attempted_user.username}', category='success')
      return redirect(url_for('market_page'))
    else: 
      flash(f'Username and password do not match! Please try again', category='danger')

  return render_template('login.html', form=form)