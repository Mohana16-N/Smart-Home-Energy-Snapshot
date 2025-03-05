from fastapi import APIRouter
from ..ml_model import predict_energy

router = APIRouter()

@router.get("/{time_of_day}")
def get_energy_prediction(time_of_day: int):
    """Predict energy consumption for a given time of day (0-23 hours)."""
    if time_of_day < 0 or time_of_day > 23:
        return {"error": "Time must be between 0 and 23 hours."}
    
    predicted_value = predict_energy(time_of_day)
    return {"time_of_day": time_of_day, "predicted_power_consumption": predicted_value}
