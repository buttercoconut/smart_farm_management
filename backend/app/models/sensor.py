from pydantic import BaseModel

class Sensor(BaseModel):
    id: int
    farm_id: int
    type: str
    location: str
