from fastapi import FastAPI
from .database import Base, engine
from .routes import devices, energy, auth, prediction

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(devices.router, prefix="/devices", tags=["Devices"])
app.include_router(energy.router, prefix="/energy", tags=["Energy Usage"])
app.include_router(prediction.router, prefix="/predict", tags=["Energy Prediction"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Home Energy API. Visit /docs for API details."}
