# actuator service with irrigation logic
from typing import List
from ..models.actuator import Actuator, ActuatorCreate

class ActuatorService:
    async def create(self, actuator: ActuatorCreate) -> Actuator:
        return Actuator(id=1, **actuator.dict())

    async def list_all(self) -> List[Actuator]:
        return []

    async def irrigate(self, farm_id: int, soil_moisture: float) -> str:
        """Core irrigation control logic.
        If soil moisture below threshold, open valve for 30s.
        """
        threshold = 30.0  # percent
        if soil_moisture < threshold:
            # send MQTT command (placeholder)
            return f"Irrigation started for farm {farm_id}"
        return f"Soil moisture sufficient ({soil_moisture}%)"
