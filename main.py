from market import app, db
from market.models import Item, User

def remove_item_by_id(item_id):
    item_to_remove = Item.query.get(item_id)
    if item_to_remove:
        db.session.delete(item_to_remove)
        db.session.commit()
        print(f"Item with ID {item_id} successfully removed.")
    else:
        print(f"Item with ID {item_id} not found.")

if __name__ == '__main__':
    with app.app_context():
        remove_item_by_id(2)
        print(__name__)
        app.run(host="0.0.0.0", port=3000, debug=True)