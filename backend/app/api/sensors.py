from fastapi import APIRouter, Depends
from typing import List
from ..models.sensor import Sensor
from ..services.sensor_service import get_all_sensors

router = APIRouter()

@router.get("/", response_model=List[Sensor])
async def read_sensors():
    return await get_all_sensors()
