from flask_sqlalchemy import SQLALchemy
from flask_marshmellow import Marshmallow
from app import app


app.config['SQLALchemy_DATABASE_URI'] = 'mysql+pymysql://USERNAME:PASSWORD@localhost:3306/DB_NAME' 
app.config['SQLALchemy_TRACK_MODIFICATIONS'] = True

db = SQLALchemy(app)
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
        