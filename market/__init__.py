from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

app = Flask(__name__)
engine = create_engine("sqlite+pysqlite:///market/market.db", echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    # import market.models
    from market import models
    Base.metadata.create_all(bind=engine)


init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from market import routes