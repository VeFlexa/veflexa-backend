from fastapi import APIRouter
from datetime import datetime
from app.utils.optimizer import generate_plan

router = APIRouter()

@router.post("/")
def optimize_charging(fleet_id: int = 1):
    plan = generate_plan(fleet_id)
    return {
        "fleet_id": fleet_id,
        "created": datetime.utcnow().isoformat(),
        "plan": plan
    }
