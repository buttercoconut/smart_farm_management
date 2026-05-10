from fastapi import FastAPI
from .app import router

app = FastAPI(title="Smart Farm Management API")
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
