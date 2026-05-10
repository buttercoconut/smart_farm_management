from fastapi import APIRouter, Depends
from typing import List
from ..models.actuator import Actuator
from ..services.actuator_service import get_all_actuators

router = APIRouter()

@router.get("/", response_model=List[Actuator])
async def read_actuators():
    return await get_all_actuators()
