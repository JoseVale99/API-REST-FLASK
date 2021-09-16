from app import app # comment this line for running!
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create models for migration in Data Base... descomment for running

# from flask import Flask
# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://YOUR_USER:YOUR_PASSWORD@localhost:3306/YOUR_DATA_BASE' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma  = Marshmallow(app)


# Create table category 
class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(110))
    cat_description = db.Column(db.String(110))

    def __init__(self, cat_name, cat_description):
        self.cat_name = cat_name
        self.cat_description = cat_description

def Update(id,cat_name, cat_description):
    category = Category.query.get(id)
    category.cat_name = cat_name
    category.cat_description = cat_description
    db.session.commit()
    return category 

def All():
    all_categorias = Category.query.all()
    result = categories_schema.dump(all_categorias) 
    return result
    
def getcatgoryID(id):
    category = Category.query.get(id)
    return category

def getcatgoryPost(cat_name,cat_description):
    new_category = Category(cat_name,cat_description)
    db.session.add(new_category)
    db.session.commit()
    return new_category
def getDelete(id):
    delete = Category.query.get(id) 
    db.session.delete(delete)
    db.session.commit()
    return delete
# Define Schema with Marshmallow
# Schema category
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_name','cat_description')

# One request
category_schema = CategorySchema()
#  Many requests
categories_schema = CategorySchema(many=True)

if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print( "Done!")

        