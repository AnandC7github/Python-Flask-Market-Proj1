from market import app, db
from market.models import Item, User

# Create a new item
new_item = Item(name='Laptop', barcode='73457980091403', price=1200, description='Discover the perfect blend of style and performance with our sleek and powerful laptop. Packed with features to enhance your computing experience, this laptop is designed to meet your every need. Key Features:Impressive Performance,Vibrant Display, Slim and Lightweight Design, Ample Storage Capacity, Long Battery Life, Connectivity Options')

if __name__ == '__main__':
  with app.app_context():
      db.session.add(new_item)
      db.session.commit()
      print(f"Item {new_item.name} added successfully!")
      print(__name__)
      app.run(host="0.0.0.0", port=3000, debug=True)