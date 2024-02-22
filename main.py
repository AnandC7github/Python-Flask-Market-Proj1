from market import app, db
from market.models import Item, User


if __name__ == '__main__':
  with app.app_context():
    # Print owner/user_id for items with IDs 1, 2, and 3
    item_ids_to_print = [1, 2, 3]

    for item_id in item_ids_to_print:
        item = Item.query.get(item_id)
        if item:
            print(f"Owner of item with ID {item_id}: {item.owner}")
    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)