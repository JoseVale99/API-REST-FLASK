from app import app
from flask import jsonify
from app.Model.models import Category,CategorySchema


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:123456789@localhost:3306/dbpythonAPI' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#  rootes API REST

# message of welcome
@app.route('/', methods=['GET'])
def index():
    return jsonify({'Message':"Welcome back!"})


# One request
category_schema = CategorySchema()
#  Many requests
categories_schema = CategorySchema(many=True)

# GET
@app.route('/category',methods=['GET'])
def get_categorias():
    all_categorias = Category.query.all()
    result = categories_schema.dump(all_categorias)
    return jsonify(result)


      


    