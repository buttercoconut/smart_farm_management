from fastapi import FastAPI
from .api import sensors, actuators, dashboard

app = FastAPI(title="Smart Farm Management API")

app.include_router(sensors.router, prefix="/sensors", tags=["Sensors"])
app.include_router(actuators.router, prefix="/actuators", tags=["Actuators"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
