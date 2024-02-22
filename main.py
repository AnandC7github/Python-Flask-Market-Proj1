from market import app, db
from market.models import Item, User

# Create a new item
new_item = Item(name='Office Chair', barcode='81735649280123', price=1200, description='Ergonomically designed seating solution crafted for optimal comfort and support during long work hours. Features adjustable height, lumbar support, and a breathable mesh backrest for enhanced productivity and well-being. Sturdy construction and contemporary design make it suitable for any modern office environment.')

if __name__ == '__main__':
  with app.app_context():
      db.session.add(new_item)
      db.session.commit()
      print(f"Item {new_item.name} added successfully!")
      print(__name__)
      app.run(host="0.0.0.0", port=3000, debug=True)