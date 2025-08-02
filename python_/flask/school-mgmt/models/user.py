from app import db
from models import BaseModel


class User(db.Model, BaseModel):
    """
    Users model
    """

    __tablename__ = 'users'

    first_name = db.Column(db.VARCHAR(128), nullable=True)
    last_name = db.Column(db.VARCHAR(128), nullable=True)
    age = db.Column(db.Integer(), nullable=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id') , nullable=True)
    student = db.relationship('Student', back_populates="user")
