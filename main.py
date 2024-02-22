from market import app, db

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
  with app.app_context():
  # Create the tables
    db.create_all()
  print(__name__)
  app.run(host="0.0.0.0", port=3000, debug=True)