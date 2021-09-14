from app import app




#  rootes API REST
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message':"Welcome!"})


    