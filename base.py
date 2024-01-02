from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fyyer:fyyer@fyyer-db:5432/fyyer'

db = SQLAlchemy(app)

migrate = Migrate(app, db)