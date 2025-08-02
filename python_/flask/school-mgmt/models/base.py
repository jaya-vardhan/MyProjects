from app import db


class BaseModel:

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    deleted = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return self.id
    
    def to_dict(self):
        data = dict()
        table_columns = self.__table__.columns.keys()

        for column in table_columns:
            data[column] = getattr(self, column, None)
        return data

    def commit(self):
        try:
            db.session.add(self)
            db.session.commit()
        except:
            raise Exception("Failed")
