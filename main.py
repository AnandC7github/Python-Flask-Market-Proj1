from market import app, db
from market.models import Item

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
    with app.app_context():
      # Drop all tables in the database
      db.drop_all()
      # Recreate the tables (if needed)
      db.create_all()
      db.session.commit()
   # Add items to the session and commit the changes
      # db.session.add_all([item1, item2, item3])
      # db.session.commit()
    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)