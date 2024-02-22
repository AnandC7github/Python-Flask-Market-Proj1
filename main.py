from market import app, db
from market.models import Item

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
   with app.app_context():
  # # Create the tables
  #   db.create_all()
  # Add items to the Item table
    item1 = Item(name='Phone', barcode='893212299897', price=500, description='Coolest phone ever')
    item2 = Item(name='Laptop', barcode='123985473165', price=900, description='Powerful laptop')
    item3 = Item(name='Keyboard', barcode='231985128446', price=150, description='Mechanical keyboard')

  # Add items to the session and commit the changes
    db.session.add_all([item1, item2, item3])
    db.session.commit()
    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)