from pydantic import BaseModel

class Farm(BaseModel):
    id: int
    name: str
    location: str
    area: float
