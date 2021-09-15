from app import app # comment this line for running!
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Create models for migration in Data Base... descomment for running

# from flask import Flask
# app = Flask(__name__)

db = SQLAlchemy(app)

# Create table category 
class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(110))
    cat_description = db.Column(db.String(110))

    def __init__(self, cat_name, cat_description):
        self.cat_name = cat_name
        self.cat_description = cat_description

ma  = Marshmallow(app)


# Define Schema with Marshmallow
# Schema category
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_name','cat_description')

if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print ("Creating database tables...")
    db.create_all()
    print( "Done!")

        