from sqlalchemy import Column, Integer, String
from market import Base

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(30), nullable=False, unique=True)
    price = Column(Integer(), nullable=False)
    barcode = Column(String(12), nullable=False, unique=True)
    description = Column(String(1024), nullable=False, unique=True)

    def __init__(self, name, price, barcode, description):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.description = description

    def __repr__(self):
        return f'<Item{self.id} {self.name} {self.price} {self.barcode} {self.description}>'