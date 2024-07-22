from sqlalchemy import Column, Integer, String, ForeignKey, orm
# from sqlalchemy.orm import relationship
from market import Base, bcrypt, login_manager, db_session
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    budget = Column(Integer(), nullable=False, default=1000)
    items = orm.relationship('Item', backref='owned_user', lazy=True)

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f'{self.budget}$'

    def __init__(self, username, email, password, budget=None):
        self.username = username
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        if budget:
            self.budget = budget

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)
    
    def can_purchase(self, item):
        return self.budget >= item.price

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
    
    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db_session.commit()
