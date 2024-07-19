from flask import Flask, render_template
app = Flask(__name__)
from database import init_db, db_session
from models import Item
init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


# item = Item('phone', 500, '893212299897', 'A UK used Iphone 30')
# db_session.add(item)
# db_session.commit()


@app.route('/') #decorator 
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