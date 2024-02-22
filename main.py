from market import app, db
from market.models import Item, User

if __name__ == '__main__':
  print(__name__)
  app.run(host="0.0.0.0", port=3000, debug=True)