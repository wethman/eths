from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# # Dependency
origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/user-token/", response_model=schemas.UserToken)
def create_user(user_token: schemas.UserTokenCreate, db: Session = Depends(get_db)):
    print(user_token)
    return crud.create_user_token(db=db, user_token=user_token)


@app.get("/user-token/", response_model=list[schemas.UserToken])
def create_user(db: Session = Depends(get_db)):
    user_token = crud.get_user_tokens(db)
    return user_token


@app.get("/")
def get_all():
    return "Hello"
