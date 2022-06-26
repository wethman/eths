from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://ytepmbbogipxds:3f36eee57816e58c506884431cc7da1469a99df22db990313bf9802290b78ed2@ec2-3-226-163-72.compute-1.amazonaws.com:5432/d2d98alpgb9ogf"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
