from flask_jwt import jsonify
from sqlalchemy.sql.functions import user
from models.category_model import CategoryModel
from flask_restful import Resource,reqparse

class Category(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = True,
        help = "Category ID cannot be blank"
    )
    parser.add_argument(
        'category_name',
        type = str,
        required = True,
        help = "Category Name cannot be blank"
    )
    
    def post(self):
        data = Category.parser.parse_args()
        categroy = CategoryModel(**data)

        if (CategoryModel.find_by_id(data['id'])):
            return {"message" : "Category Id is already exists!"}, 400

        try:
            categroy.save_to_db()
            return {'Massage' : "Category Created Successfully"}, 200
        except:
            return {'Massage' : "An error occured while inserting to database"}, 500
        
    
    def delete(self):
        data = Category.parser.parse_args()
        user = CategoryModel.find_by_id(data["id"])
        if user:
            user.delete_from_db()
            return {"Massage" : "{} has been deleted".format(data["id"])}, 200
        
        return {"Massage" : "An error occurs while deleting user"}, 500
    
    def put(self):
        data = Category.parser.parse_args()
        category = CategoryModel.find_by_id(data["id"])
        
        if category:
            category = CategoryModel(data["id"],data["name"])
        else:
            category.id = data["id"]
            category.name = data["name"]
        
        category.save_to_db()
        
        return category.json(), 200
    
class AllCategory(Resource):
    def get(self):
        categories = CategoryModel.query.all()
        return { "All Categories" : [ category.json() for category in categories ]}