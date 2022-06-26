from lib2to3.pgen2 import token
from sqlalchemy.orm import Session

from . import models, schemas


def get_user_tokens(db: Session) -> list[schemas.UserToken]:
    return db.query(models.UserToken).all()


def create_user_token(db: Session, user_token: schemas.UserTokenCreate):
    db_user_token = models.UserToken(
        address=user_token.address, token_type=user_token.token_type, token_address=user_token.token_address, date=user_token.date, token_id=user_token.token_id)
    db.add(db_user_token)
    db.commit()
    db.refresh(db_user_token)
    return db_user_token
