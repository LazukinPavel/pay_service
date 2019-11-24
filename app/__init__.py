import os

from flask import Flask
from flask_bootstrap import Bootstrap
import logging.handlers

from .config import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
bootstrap = Bootstrap(app)


if not os.path.exists('logs'):
    os.mkdir('logs')

handler = logging.handlers.RotatingFileHandler(
        'logs/pay.log',
        maxBytes=1024 * 1024)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


from app import routes


if __name__ == '__main__':
    app.run()

