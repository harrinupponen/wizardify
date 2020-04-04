from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(Config)

# With the extension initialized, a bootstrap/base.html
# template becomes available, and can be referenced from
# application templates with the extends clause.
bootstrap = Bootstrap(app)

from app import routes

