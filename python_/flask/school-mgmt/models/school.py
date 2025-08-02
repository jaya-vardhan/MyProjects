from app import db
from models import BaseModel


class School(db.Model, BaseModel):

    __tablename__ = 'schools'

    name = db.Column(db.VARCHAR(128), nullable=True)
    address = db.Column(db.Text(), nullable=True)
    student = db.relationship('Student', back_populates="school")

