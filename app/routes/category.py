from app import app
from flask import jsonify

#  rootes API REST

# message of welcome
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message':"Welcome back!"})





    