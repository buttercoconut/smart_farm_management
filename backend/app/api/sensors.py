# sensors API
from fastapi import APIRouter, Depends
from ..models.sensor import SensorCreate, Sensor
from ..services.sensor_service import SensorService

router = APIRouter()

@router.post("/", response_model=Sensor)
async def create_sensor(sensor: SensorCreate, service: SensorService = Depends()):
    return await service.create(sensor)

@router.get("/", response_model=list[Sensor])
async def list_sensors(service: SensorService = Depends()):
    return await service.list_all()
