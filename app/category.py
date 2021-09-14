from app import app
from flask import jsonify


#  rootes API REST
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message':"Welcome!"})





    