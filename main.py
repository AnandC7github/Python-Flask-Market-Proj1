from market import app, db
from market.models import Item, User


if __name__ == '__main__':
  # with app.app_context():
  #   # Remove item with ID 2
  #   item_to_remove_2 = Item.query.get(2)
  #   db.session.delete(item_to_remove_2)

  #   # Remove item with ID 5
  #   item_to_remove_5 = Item.query.get(5)
  #   db.session.delete(item_to_remove_5)

  #   db.session.commit()
  print(__name__)
  app.run(host="0.0.0.0", port=3000, debug=True)