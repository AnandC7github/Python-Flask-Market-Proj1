from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)


class Item(db.Model):
  """Database table for ITEMS"""
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), nullable=False)
  barcode = db.Column(db.String(), nullable=False)
  price = db.Column(db.Integer(), nullable=False)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'Item {self.name}'


@app.route(
    '/'
)  # python decorators - What url in your website i am going to navigate through
@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market')
def market_page():
  items = [{
      'id': 1,
      'name': 'Phone',
      'barcode': '893212299897',
      'price': 500
  }, {
      'id': 2,
      'name': 'Laptop',
      'barcode': '123985473165',
      'price': 900
  }, {
      'id': 3,
      'name': 'Keyboard',
      'barcode': '231985128446',
      'price': 150
  }]
  return render_template('market.html', items=items)


if __name__ == '__main__':

  #DATA-BASE CODE HERE --------------------------
  with app.app_context():
    # # drop the database tables
    db.drop_all()
    # # create database and table
    db.create_all()

  app.run(host='0.0.0.0', port=3000, debug=True)
