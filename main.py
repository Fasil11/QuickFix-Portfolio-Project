from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@host/database'
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app import views, auths, models

if __name__ == '__main__':
    app.run(debug=True)