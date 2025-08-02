from app import db
from models import BaseModel


class Student(db.Model, BaseModel):
    """
    Students model
    """

    __tablename__ = 'students'

    name = db.Column(db.VARCHAR(128), nullable=True)
    roll_no = db.Column(db.Integer(), nullable=True)
    school_id = db.Column(db.Integer(), db.ForeignKey('schools.id') , nullable=True)
    school = db.relationship('School', back_populates="student")
    marks = db.relationship('Marks', back_populates="student")
    user = db.relationship('User', uselist=False, back_populates="student") #uselist=False, to make one-one
