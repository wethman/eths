from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://uikssbxibhfwjl:b1c5d500d5a3540f75e159111460e0b536a26947775c56d5560ce209a0efad66@ec2-34-239-241-121.compute-1.amazonaws.com:5432/d7jsk9m1es8j7a"
# SQLALCHEMY_DATABASE_URL = ://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
