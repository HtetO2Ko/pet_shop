from db import db

class CategoryModel(db.Model):
    
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(30))
    
    @classmethod
    def find_by_name(cls,categoryname):
        return cls.query.filter_by(category_name=categoryname).first()
    
    @classmethod
    def find_by_id(cls,categoryid):
        return cls.query.filter_by(id=categoryid).first()

    def json(self):
        return {"category_id" : self.id, 'category_name' : self.category_name}
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
