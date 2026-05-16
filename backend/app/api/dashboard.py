# dashboard API placeholder
from fastapi import APIRouter

router = APIRouter()

@router.get("/metrics")
async def get_metrics():
    return {"message": "Dashboard metrics placeholder"}
