from pydantic import BaseModel

class Price(BaseModel):
    hour: str
    value: float

    class Config:
        orm_mode = True
