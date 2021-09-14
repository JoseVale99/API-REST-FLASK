from app import app
from flask import jsonify
from flask_sqlalchemy import SQLALchemy
from flask_marshmellow import Marshmallow

#  rootes API REST

# message of welcome
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message':"Welcome!"})





    