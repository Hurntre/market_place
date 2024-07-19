from market import app
from flask import render_template
from market.models import Item



@app.route('/')
@app.route('/home')
def home_page():
  return render_template('home.html')

@app.route('/market')
def market_page():

  items = Item.query.all()
  return render_template('market.html', items=items)

@app.route('/about/<username>')
def about_page(username):
    return f'<h1>This is the about page of {username}</h1>'


# item = Item('phone', 500, '893212299897', 'A UK used Iphone 30')
# db_session.add(item)
# db_session.commit()