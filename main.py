from market import app, db
from market.models import Item, User


# Create a new user
new_user = User(username='Anand', email_address='anand@gmail.com', password_hash='123456', budget=150000)

#checks if the run.py has executed directly and not imported 
if __name__ == '__main__':
  # Add the new user to the database
  with app.app_context():
    db.session.add(new_user)
    db.session.commit()

    print(__name__)
    print(f"User {new_user.username} added successfully!")
    app.run(host="0.0.0.0", port=3000, debug=True)