from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thunyaung:@localhost/pet_shop'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
try:
    prodURI = os.getenv("DATABASE_URL")
    prodURI = prodURI.replace("postgres://dxjrizgzjdbdzh:59030e5ca42910275bbdd2dd0276e28eb7fac720be1045b2d58b9262e5706688@ec2-52-23-131-232.compute-1.amazonaws.com:5432/df1quashfuerja", "postgres://dxjrizgzjdbdzh:59030e5ca42910275bbdd2dd0276e28eb7fac720be1045b2d58b9262e5706688@ec2-52-23-131-232.compute-1.amazonaws.com:5432/df1quashfuerja")
    app.config['SQLALCHEMY_DATABASE_URI'] = prodURI
except:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thunyaung:@localhost/pet_shop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "my_pet_is_your_pet"
api = Api(app)

db = SQLAlchemy(app)