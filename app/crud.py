from sqlalchemy.orm import Session
from . import models, schemas

def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = models.Device(name=device.name, location=device.location)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device

def get_devices(db: Session):
    return db.query(models.Device).all()

def log_energy_usage(db: Session, usage: schemas.EnergyUsageCreate):
    db_usage = models.EnergyUsage(device_id=usage.device_id, power_consumed=usage.power_consumed)
    db.add(db_usage)
    db.commit()
    db.refresh(db_usage)
    return db_usage

def get_energy_usage(db: Session, device_id: int):
    return db.query(models.EnergyUsage).filter(models.EnergyUsage.device_id == device_id).all()
