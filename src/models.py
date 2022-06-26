from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base


class UserToken(Base):
    __tablename__ = "usertokens"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    token_type = Column(String, index=True)
    token_address = Column(String, index=True)
    token_id = Column(String, index=True)
    date = Column(String, index=True)
    
