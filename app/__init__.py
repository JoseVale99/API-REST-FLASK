from flask import Flask

app = Flask(__name__)

from app.routes.category import category


