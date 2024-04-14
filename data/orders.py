import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Orders(SqlAlchemyBase):
    __tablename__ = 'orders'

    order_id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    item_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("items.article"))
    size = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    orderer = orm.relationship('User')

    def __repr__(self):
        return f'<Orderd> {self.orderer} {self.order_id} {self.item_id}'