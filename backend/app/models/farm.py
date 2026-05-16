# farm model
from pydantic import BaseModel

class FarmBase(BaseModel):
    name: str
    location: str
    area: float

class FarmCreate(FarmBase):
    pass

class Farm(FarmBase):
    id: int

    class Config:
        orm_mode = True
