from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

# Mock temporal — sustituiremos con datos reales del fetcher ESIOS
@router.get("/")
def get_prices():
    now = datetime.utcnow()
    prices = [
        {"timestamp": (now + timedelta(hours=i)).isoformat(), "price_eur_mwh": 100 + i*2}
        for i in range(24)
    ]
    return {"count": len(prices), "data": prices}
