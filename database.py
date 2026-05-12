from sqlmodel import create_engine, Session, SQLModel
from models import Usuarios

DATABASE_URI = 'mysql+pymysql://root:admin@localhost:3306/ecommerce'

engine = create_engine(DATABASE_URI)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session