from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sign(db.Model):
    id = db.Column(db.String, primary_key=True)
    business_name = db.Column(db.String(80), nullable=False)
    hours = db.Column(db.String(120), nullable=False)
