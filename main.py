from market import app, db
from market.models import Item, User


if __name__ == '__main__':
  with app.app_context():
  # Change ID of item 3 to 2
    item_to_update_3 = Item.query.get(3)
    if item_to_update_3:
        item_to_update_3.id = 2

  # Change ID of item 4 to 3
    item_to_update_4 = Item.query.get(4)
    if item_to_update_4:
      item_to_update_4.id = 3

  db.session.commit()
  print(__name__)
  app.run(host="0.0.0.0", port=3000, debug=True)