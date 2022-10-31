from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()
