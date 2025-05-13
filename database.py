from sqlalchemy import create_engine, Column, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class BaseModel(declarative_base()):
    __abstract__ = True
    
    id = Column(Integer, primary_key=True, index=True)
    is_active = Column(Boolean, default=True)

    
SQLALCHEMY_DATABASE_URL = "sqlite:///.order.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={'check_same_thread': False}
)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)
Base = declarative_base(cls=BaseModel)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()