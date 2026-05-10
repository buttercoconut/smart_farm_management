from fastapi import APIRouter
from .api import sensors, actuators, dashboard

router = APIRouter()
router.include_router(sensors.router, prefix="/sensors", tags=["sensors"])
router.include_router(actuators.router, prefix="/actuators", tags=["actuators"])
router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
