from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def list_chargers():
    return {"message": "Chargers endpoint pending implementation"}
