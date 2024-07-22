from sqlalchemy import Column, Integer, String, ForeignKey, orm
# from sqlalchemy.orm import relationship
from market import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    budget = Column(Integer(), nullable=False, default=1000)
    items = orm.relationship('Item', backref='owned_user', lazy=True)

    def __init__(self, username, email, password, budget=1000):
        self.username = username
        self.email = email
        self.password = password
        self.budget = budget

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    price = Column(Integer(), nullable=False)
    barcode = Column(String(12), nullable=False, unique=True)
    description = Column(String(1024), nullable=False, unique=True)
    owner = Column(Integer(), ForeignKey('users.id'))

    def __init__(self, name, price, barcode, description):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.description = description

    def __repr__(self):
        return f'Item {self.name} {self.price} {self.barcode} {self.description}'