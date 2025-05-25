from fastapi import APIRouter
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/predict-price/{produce}")
def predict_price(produce: str):
    today = datetime.now()
    return {
        "produce": produce,
        "predictions": [
            {"date": (today + timedelta(days=i)).strftime("%Y-%m-%d"), "price": round(100 + i * 2.5, 2)}
            for i in range(7)
        ]
    }
