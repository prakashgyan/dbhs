from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sign(db.Model):
    id = db.Column(db.String, primary_key=True)
    opening_time = db.Column(db.String(30), nullable=False)
    closing_time = db.Column(db.String(30), nullable=False)
    is_open_monday = db.Column(db.Boolean, nullable=False)
    is_open_tuesday = db.Column(db.Boolean, nullable=False)
    is_open_wednesday = db.Column(db.Boolean, nullable=False)
    is_open_thursday = db.Column(db.Boolean, nullable=False)
    is_open_friday = db.Column(db.Boolean, nullable=False)
    is_open_saturday = db.Column(db.Boolean, nullable=False)
    is_open_sunday = db.Column(db.Boolean, nullable=False)

