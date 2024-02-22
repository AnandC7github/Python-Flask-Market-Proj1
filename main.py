from market import app, db
from market.models import Item


#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
  with app.app_context():
    # drop the database tables
    db.drop_all()
    # create database and table
    db.create_all()
    print(__name__)
    app.run(host="0.0.0.0", port=3000, debug=True)