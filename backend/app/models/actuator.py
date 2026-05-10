from pydantic import BaseModel

class Actuator(BaseModel):
    id: int
    farm_id: int
    type: str
    location: str
