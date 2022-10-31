from db import db

class PetModel(db.Model):
    
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db.Column(db.String(30))
    info = db.Column(db.String(30))
    price = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(pet_name=name).first()
    
    @classmethod
    def find_by_id(cls,pet_id):
        return cls.query.filter_by(id=pet_id).first()

    def json(self):
        return {"pet_id" : self.id, 'pet_name' : self.pet_name, 'price' : self.price, "info" : self.info, "user_id" : self.user_id, "category_id" : self.category_id }
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

# id
# pet_name
# info
# price
# user_id
# category_id

