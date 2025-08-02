from app import db
from models import BaseModel


class Marks(db.Model, BaseModel):

    __tablename__ = 'marks'

    subject = db.Column(db.VARCHAR(64), nullable=True)
    total_marks = db.Column(db.Integer(), nullable=True)
    marks_obtained = db.Column(db.Integer(), nullable=True)
    grade = db.Column(db.VARCHAR(8), nullable=True)
    student_id = db.Column(db.Integer(), db.ForeignKey('students.id') ,nullable=True)
    student = db.relationship('Student', back_populates="marks")

