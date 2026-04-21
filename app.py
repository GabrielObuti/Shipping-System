from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum
from main import ground_shipping, drone_shipping

app = FastAPI()

class ShippingType(str, Enum):
    ground = "ground"
    drone = "drone"
    premium = "premium"

class ShippingRequest(BaseModel):
    weight: float
    shipping_type: ShippingType


@app.post("/shipping")
def shipping(request: ShippingRequest):
    if request.weight <= 0: raise HTTPException(status_code=400, detail="Weight must be positive!")

    costs = {
        "ground": ground_shipping(request.weight),
        "premium": 125.00,
        "drone": drone_shipping(request.weight)
    }

    cheapest_method = min(costs, key=costs.get)

    return {
        "input": {
            "weight": request.weight
        },
        "options": costs,
        "cheapest": {
            "method": cheapest_method,
            "price": costs[cheapest_method]
        }
    }
