# actuator model
from pydantic import BaseModel

class ActuatorBase(BaseModel):
    name: str
    type: str
    location: str
    farm_id: int

class ActuatorCreate(ActuatorBase):
    pass

class Actuator(ActuatorBase):
    id: int

    class Config:
        orm_mode = True
