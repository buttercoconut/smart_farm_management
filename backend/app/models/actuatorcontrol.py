from pydantic import BaseModel
from datetime import datetime

class ActuatorControl(BaseModel):
    id: int
    actuator_id: int
    command: str
    timestamp: datetime
