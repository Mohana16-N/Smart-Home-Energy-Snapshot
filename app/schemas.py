from pydantic import BaseModel
from datetime import datetime

class DeviceCreate(BaseModel):
    name: str
    location: str

class DeviceResponse(DeviceCreate):
    id: int
    class Config:
        from_attributes = True

class EnergyUsageCreate(BaseModel):
    device_id: int
    power_consumed: float

class EnergyUsageResponse(EnergyUsageCreate):
    id: int
    timestamp: datetime
    class Config:
        from_attributes = True
