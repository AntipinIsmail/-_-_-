import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Items(SqlAlchemyBase):
    __tablename__ = 'items'

    article = sqlalchemy.Column(sqlalchemy.Integer,
                                primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
#type = orm.relationship("Types")
   # type_id = sqlalchemy.Column(sqlalchemy.Integer,
                               # sqlalchemy.ForeignKey("types.id"))
    user = orm.relationship('User')
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    about = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    price = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    picture = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    orders = orm.relationship("Orders", back_populates='item')

    def __repr__(self):
        return f'<Created> {self.creator} {self.name} {self.article}'

    def convertToBinaryData(self, picture):
        # Convert digital data to binary format
        with open(picture, 'rb') as file:
            blobData = file.read()
        self.picture = blobData

    def convertToPicture(data, picture):
        # Convert binary data to proper format and write it on Hard Disk
        with open(picture, 'wb') as file:
            file.write(data)
