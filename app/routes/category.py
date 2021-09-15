from app import app
from flask import jsonify, request
from app.Model.models import Category,CategorySchema
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:123456789@localhost:3306/dbpythonAPI' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
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
def getCategories():
    all_categorias = Category.query.all()
    result = categories_schema.dump(all_categorias)
    return jsonify(result)

#  GET for ID
@app.route('/category/<id>', methods=['GET'])      
def getCategoryID(id):
    category = Category.query.get(id)
    return category_schema.jsonify(category)
    
#  POST
@app.route('/categories', methods=['POST'])
def categoryNew():
    data = request.get_json(force=True)
    cat_name = data['cat_name']
    cat_description = data['cat_description']
    
    new_category = Category(cat_name,cat_description)
    db.session.add(new_category)
    db.session.commit()
    return category_schema.jsonify(new_category)
    
    

    