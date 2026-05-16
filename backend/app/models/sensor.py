# sensor model
from pydantic import BaseModel

class SensorBase(BaseModel):
    name: str
    type: str
    location: str
    farm_id: int

class SensorCreate(SensorBase):
    pass

class Sensor(SensorBase):
    id: int

    class Config:
        orm_mode = True
