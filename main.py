from market import app, db
from market.models import Item, User


# Create a new item
new_item = Item()
new_item.name = 'Projector'
new_item.barcode = '75611239876173'
new_item.price = 15000
new_item.description = 'Unlock an immersive cinematic experience within the comfort of your home with our High-Definition Home Theater Projector. Elevate your movie nights, gaming sessions, and presentations to a whole new level of brilliance and clarity. Key Features : Crystal Clear Visuals, Powerful Brightness, Versatile Connectivity, Cinematic Sound, User-Friendly Controls, Compact and Portable and Extended Lamp Life.'

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
  # Add the new user to the database
  with app.app_context():
    db.session.add(new_item)
    db.session.commit()

    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)