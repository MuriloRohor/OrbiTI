import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.sql.models.Base import Base

@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield Session()
    Base.metadata.drop_all(engine)
