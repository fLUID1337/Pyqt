import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

sqlalchemy_base=dec.declarative_base()
factory=None

def global_init():
    global factory
    if factory:
        return
    con=f"postgresql+psycopg2://postgres:Martin131214@localhost/agario"
    engine=sa.create_engine(con,echo=False)
    factory=orm.sessionmaker(bind=engine)
    from . import all_models
    sqlalchemy_base.metadata.create_all(engine)

def create_session()->Session:
    global factory
    return factory()    