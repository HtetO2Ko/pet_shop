from flask_jwt import jsonify
from sqlalchemy.sql.functions import user
from flask_restful import Resource,reqparse
from models.pets_model import PetModel
from models.user_model import UserModel
from models.category_model import CategoryModel

class Pet(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = True,
        help = "Pet ID cannot be blank"
    )
    parser.add_argument(
        'pet_name',
        type = str,
        required = True,
        help = "Pet Name cannot be blank"
    )
    parser.add_argument(
        'info',
        type = str,
        required = True,
        help = "Information cannot be blank"
    )
    parser.add_argument(
        'price',
        type = int,
        required = True,
        help = "Price cannot be blank"
    )
    parser.add_argument(
        'user_id',
        type = int,
        required = True,
        help = "User ID cannot be blank"
    )
    parser.add_argument(
        'category_id',
        type = int,
        required = True,
        help = "Category ID cannot be blank"
    )
    
    def post(self):
        data = Pet.parser.parse_args()
        pet = PetModel(**data)

        if (PetModel.find_by_id(data['id'])):
            return {"message" : "Pet Id is already exists!"}, 400

        try:
            pet.save_to_db()
            return {'Massage' : "Pet Created Successfully"}, 200
        except:
            return {'Massage' : "Create Error"}, 500
        
    
    def delete(self):
        data = Pet.parser.parse_args()
        pet = PetModel.find_by_id(data["id"])
        if pet:
            pet.delete_from_db()
            return {"Massage" : "{} has been deleted".format(data["id"])}, 200
        
        return {"Massage" : "Pet Not Found"}, 500
    
    def put(self):
        data = Pet.parser.parse_args()
        pet = PetModel(**data)
        
        if pet is None:
            pet = PetModel(data["id"],data["pet_name"], data["info"], data["price"], data["user_id"], data["category_id"])
            return {'Massage' : "Pet Created Successfully"}, 200
        else:
            pet.id = data["id"]
            pet.pet_name = data["pet_name"]
            pet.info = data["info"]
            pet.price = data["price"]
            pet.user_id = data["user_id"]
            pet.category_id = data["category_id"]
            pet.save_to_db()
            return {'Massage' : "Pet Updated Successfully"}, 200
    
# id
# pet_name
# info
# price
# user_id
# category_id
    
class AllPets(Resource):
    def get(self):
        pets = PetModel.query.all()
        return { "All Pets" : [ pet.json() for pet in pets ]}