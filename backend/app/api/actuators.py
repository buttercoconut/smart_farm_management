# actuators API
from fastapi import APIRouter, Depends
from ..models.actuator import ActuatorCreate, Actuator
from ..services.actuator_service import ActuatorService

router = APIRouter()

@router.post("/", response_model=Actuator)
async def create_actuator(actuator: ActuatorCreate, service: ActuatorService = Depends()):
    return await service.create(actuator)

@router.get("/", response_model=list[Actuator])
async def list_actuators(service: ActuatorService = Depends()):
    return await service.list_all()
