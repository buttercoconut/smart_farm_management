# sensor service
from typing import List
from ..models.sensor import Sensor, SensorCreate

class SensorService:
    async def create(self, sensor: SensorCreate) -> Sensor:
        # placeholder logic
        return Sensor(id=1, **sensor.dict())

    async def list_all(self) -> List[Sensor]:
        return []
