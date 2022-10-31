from db import db

class UserModel(db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))
    usertype = db.Column(db.String(30))
    
    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(username=name).first()
    
    @classmethod
    def find_by_id(cls,userid):
        return cls.query.filter_by(id=userid).first()

    def json(self):
        return {'id' : self.id ,  'username' : self.username, 'password' : self.password, "usertype" : self.usertype }
        
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
