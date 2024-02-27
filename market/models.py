from market import db, login_manager
from market import bcrypt

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  username = db.Column(db.String(length=100), nullable=False)
  email_address = db.Column(db.String(length=100), nullable=False, unique = True)
  password_hash = db.Column(db.String(length=100), nullable=False)
  budget = db.Column(db.Integer(), nullable=False, default = 100000)
  items = db.relationship('Item', backref='owned_user',lazy = True)

  @property
  def password(self):
    return self.password
  
  @password.setter
  def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
  def check_password_correction(self, attempted_password):
    return bcrypt.check_password_hash(self.password_hash, attempted_password)

class Item(db.Model):
    """Database table for ITEMS"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    barcode = db.Column(db.String(14), nullable=False)
    price = db.Column(db.Integer(), nullable=False, info={'check_constraint': 'price >= 100'})
    description = db.Column(db.String(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'
