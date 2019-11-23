import os

from flask import Flask
from flask_bootstrap import Bootstrap
import logging

from .config import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
bootstrap = Bootstrap(app)


if not os.path.exists('logs'):
    os.mkdir('logs')
logging.basicConfig(filename='logs/pay.log', level=logging.INFO)


from app import routes

