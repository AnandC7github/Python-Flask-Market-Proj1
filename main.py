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

  def __repr__(self) -> str:
    return f"ITEM < {self.name} | ${self.price} >"


@app.route(
    '/'
)  # python decorators - What url in your website i am going to navigate through
@app.route('/home')
def home_page():
  return render_template('home.html')


@app.route('/market')
def market_page():
  # items = [{
  #     'id': 1,
  #     'name': 'Phone',
  #     'barcode': '893212299897',
  #     'price': 500
  # }, {
  #     'id': 2,
  #     'name': 'Laptop',
  #     'barcode': '123985473165',
  #     'price': 900
  # }, {
  #     'id': 3,
  #     'name': 'Keyboard',
  #     'barcode': '231985128446',
  #     'price': 150
  # }]
  items = Item.query.all()
  return render_template('market.html', items=items)


if __name__ == '__main__':

  #DATA-BASE CODE HERE --------------------------
  with app.app_context():
    # # drop the database tables
    db.drop_all()
    # # create database and table
    db.create_all()
    print(">> Database :: <<")
    # # Add an item into the ITEM table
    item = Item()
    item.name = 'Phone X'
    item.barcode = '893212299889'
    item.price = 600
    item.description = 'Coolest phone X ever'

    db.session.add(item)
    db.session.commit()

    # Different Syntax ---
    item_1 = Item(name='Phone',
                  barcode='893212299897',
                  price=500,
                  description='Coolest phone ever')
    item_2 = Item(name='Laptop',
                  barcode='993212299897',
                  price=1500,
                  description='Coolest Laptop ever')
    item_3 = Item(name='Apple Laptop',
                  barcode='993212299999',
                  price=2500,
                  description='Coolest Apple Laptop ever')
    item_4 = Item(name='Gameboy',
                  barcode='993212299897',
                  price=150,
                  description='Coolest Gameboy ever')
    db.session.add_all([item_1, item_2, item_3, item_4])
    db.session.commit()

    # # print all the items in the table ITEM
    # print(Item.query.all())
    for item in Item.query.all():
      print(">> ", item)

  # -------------------------------------------------------------

  app.run(host='0.0.0.0', port=3000, debug=True)
