from fastapi import APIRouter, Depends
from typing import List
from ..models.farm import Farm
from ..services.dashboard_service import get_farm_dashboard

router = APIRouter()

@router.get("/", response_model=List[Farm])
async def read_dashboard():
    return await get_farm_dashboard()
