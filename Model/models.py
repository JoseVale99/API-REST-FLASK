from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:123456789@localhost:3306/dbpythonAPI' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
ma  = Marshmallow(app)

#  Model of category objects
class Category(db.Model):
    cat_id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(100))
    cat_description = db.Column(db.String(100))

    def __init__(self, cat_name, cat_description):
        self.cat_name = cat_name
        self.cat_description = cat_description

db.create_all()
        