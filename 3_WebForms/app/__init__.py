from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from.from_object(Config)

from app import routes
