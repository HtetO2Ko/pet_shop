from db import *
from resource.category_resource import AllCategory, Category
from resource.pets_resource import AllPets, Pet
from resource.user_resource import AllUser, User

api.add_resource(User, "/user")
api.add_resource(AllUser, "/allusers")

api.add_resource(Category, "/category")
api.add_resource(AllCategory, "/allcategories")

api.add_resource(Pet, "/pet")
api.add_resource(AllPets, "/allpets")

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True , port=5000)
