from market import db 

class User(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(length=100), nullable=False)

class Item(db.Model):
    """Database table for ITEMS"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    barcode = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'Item {self.name}'
