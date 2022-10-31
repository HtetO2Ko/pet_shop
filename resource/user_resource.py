from flask_jwt import jsonify
from sqlalchemy.sql.functions import user
from models.user_model import UserModel
from flask_restful import Resource,reqparse

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = False,
        help = "User ID cannot be blank"
    )
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "User Name cannot be blank"
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "Password cannot be blank"
    )
    parser.add_argument(
        'usertype',
        type = str,
        required = True,
        help = "User Type cannot be blank"
    )
    
    def post(self):
        data = User.parser.parse_args()
        if (UserModel.find_by_id(data['id'])):
            return {"message" : "User Id is already exists!"}, 400
        user = UserModel(**data)

        try:
            user.save_to_db()
            return {'Massage' : "User Created Successfully"}, 200
        except:
            return {'Massage' : "An error occured while inserting to database"}, 500
        
    
    def delete(self):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data["id"])
        if user:
            user.delete_from_db()
            return {"Massage" : "{} has been deleted".format(data["id"])}, 200
        
        return {"Massage" : "An error occurs while deleting user"}, 500
    
    def put(self):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data["id"])
        
        if user is None:
            user = UserModel(data["id"],data["username"],data["password"],data["usertype"])
        else:
            user.id = data["id"]
            user.username = data["username"]
            user.password = data["password"]
            user.usertype = data["usertype"]
        
        user.save_to_db()
        
        return user.json(), 200
    
class AllUser(Resource):
    def get(self):
        users = UserModel.query.all()
        return { "All User" : [ user.json() for user in users ]}