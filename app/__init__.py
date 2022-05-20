from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap


# create instance of app
app = Flask(__name__)

# import config
app.config.from_object(Config)

# initialize db
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# initialize bootstrap
bootstrap = Bootstrap(app)

from app import routes, models