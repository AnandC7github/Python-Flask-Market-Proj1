from market import app, db
from market.models import Item

# List of item IDs to delete
item_ids_to_delete = [7, 8, 9]

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
    with app.app_context():
      # Iterate over the item IDs and delete each item
      for item_id in item_ids_to_delete:
          item_to_delete = Item.query.get(item_id)

          # Check if the item with the given ID exists
          if item_to_delete:
              db.session.delete(item_to_delete)
              print(f"Deleted item with ID {item_id}")
          else:
              print(f"Item with ID {item_id} not found in the database")

      # Commit the changes to the database
      db.session.commit()
    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)