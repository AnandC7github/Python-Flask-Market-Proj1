from market import app, db
from market.models import Item, User


if __name__ == '__main__':
  with app.app_context():
  # Update owner/user_id for items in the database
    items_to_update = Item.query.all()
    for item in items_to_update:
      item.owner = 1
    db.session.commit()
    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)