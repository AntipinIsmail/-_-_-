import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Items(SqlAlchemyBase):
    __tablename__ = 'items'

    article = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("types.id"))
    #creator = orm.relationship('User')
    price = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    picture = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    def __repr__(self):
        return f'<Created> {self.article} {self.name} {self.price}'

    def convertToBinaryData(self, picture):
        # Convert digital data to binary format
        with open(picture, 'rb') as file:
            blobData = file.read()
        self.picture = blobData

    def convertToPicture(data, picture):
        # Convert binary data to proper format and write it on Hard Disk
        with open(picture, 'wb') as file:
            file.write(data)


