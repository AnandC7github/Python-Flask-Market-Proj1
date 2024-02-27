from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'b5d9ed02db8471d660ba4e35'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) # creating an instance
login_manager = LoginManager(app)
from market import routes
