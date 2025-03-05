from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.EnergyUsageResponse)
def log_energy(usage: schemas.EnergyUsageCreate, db: Session = Depends(database.get_db)):
    return crud.log_energy_usage(db, usage)

@router.get("/{device_id}", response_model=list[schemas.EnergyUsageResponse])
def get_energy(device_id: int, db: Session = Depends(database.get_db)):
    return crud.get_energy_usage(db, device_id)
