from pydantic import BaseModel


class UserTokenBase(BaseModel):
    address: str
    token_type: str
    token_address: str
    token_id: str
    date: str


class UserToken(UserTokenBase):
    id: int

    class Config:
        orm_mode = True


class UserTokenCreate(UserTokenBase):
    pass
