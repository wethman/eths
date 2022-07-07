from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://oiycvtfwhxngou:3de927a50541e4167625454cf645e7e29c37ac201bb6dce8254eef593f86d7b3@ec2-44-205-41-76.compute-1.amazonaws.com:5432/d2lq4sjklblcag"
# SQLALCHEMY_DATABASE_URL = ://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
