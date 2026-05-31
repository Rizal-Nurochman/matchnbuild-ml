from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from database import get_design_items
from services.vectorizer import compute_min_max, vectorize_item, vectorize_input

# Field numerik yang akan divektorkan
NUMERIC_FIELDS = [
    "estimated_budget", "land_area_min", "building_area",
    "num_floors", "num_bedrooms", "room_area"
]

def get_recommendations(user_input: dict, category: str = None, limit: int = 10):
    items = get_design_items(category)
    if not items:
        return []

    ranges = compute_min_max(items, NUMERIC_FIELDS)

    user_vector = vectorize_input(user_input, ranges)

    user_vector = user_vector.reshape(1, -1)

    item_vectors = np.array([vectorize_item(item, ranges) for item in items])

    scores = cosine_similarity(user_vector, item_vectors)[0]

    results = []
    for i, item in enumerate(items):
        results.append({
            "item_id": str(item["id"]),
            "score": round(float(scores[i]), 4)
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    results = [r for r in results if r["score"] > 0]

    return results[:limit]