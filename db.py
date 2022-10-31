from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thunyaung:@localhost/pet_shop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "my_pet_is_your_pet"
api = Api(app)

db = SQLAlchemy(app)