from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/", response_model=schemas.DeviceResponse)
def create_device(device: schemas.DeviceCreate, db: Session = Depends(database.get_db)):
    return crud.create_device(db, device)

@router.get("/", response_model=list[schemas.DeviceResponse])
def get_all_devices(db: Session = Depends(database.get_db)):
    return crud.get_devices(db)
