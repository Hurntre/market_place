from market import app, db_session
from flask import render_template, redirect, url_for
from market.models import Item, User
from market.forms import RegisterForm


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
      print(f'There was an error while attempting to register new user: {err_msg}')
  return render_template('register.html', form=form)
