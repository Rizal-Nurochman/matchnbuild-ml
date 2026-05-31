from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from services.recommender import get_recommendations

router = APIRouter()

class RecommendRequest(BaseModel):
    category: Optional[str] = None
    style: Optional[str] = None
    location: Optional[str] = None
    estimated_budget: Optional[float] = 0
    land_area_min: Optional[float] = 0
    land_area_max: Optional[float] = 0
    building_area: Optional[float] = 0
    num_floors: Optional[int] = 0
    num_bedrooms: Optional[int] = 0
    room_type: Optional[str] = None
    room_area: Optional[float] = 0
    limit: Optional[int] = 10

class RecommendResponse(BaseModel):
    item_id: str
    score: float

@router.post("/api/recommend", response_model=list[RecommendResponse])
def recommend(req: RecommendRequest):
    user_input = req.model_dump(exclude={"category", "limit"})
    results = get_recommendations(user_input, category=req.category, limit=req.limit)
    return results
