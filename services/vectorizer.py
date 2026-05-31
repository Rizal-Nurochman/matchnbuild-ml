import numpy as np

STYLES = ["minimalist", "tropical", "scandinavian", "industrial", "classic", "japandi", "modern"]
LOCATIONS = ["Jakarta", "Bandung", "Surabaya", "Bali", "Yogyakarta"]

def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0.0
    return (value - min_val) / (max_val - min_val)


def one_hot(value, categories):
    vector = [0.0] * len(categories)
    if value in categories:
        vector[categories.index(value)] = 1.0
    return vector


def compute_min_max(items, fields):
    ranges = {}
    for field in fields:
        values = [float(item.get(field) or 0) for item in items]
        ranges[field] = (min(values), max(values))
    return ranges


def vectorize_item(item, ranges):
    vector = []

    numeric_fields = ["estimated_budget", "land_area_min", "building_area", "num_floors", "num_bedrooms", "room_area"]
    
    for field in numeric_fields:
        value = float(item.get(field) or 0)
        min_val, max_val = ranges[field]
        vector.append(normalize(value, min_val, max_val))

    vector.extend(one_hot(item.get("style", ""), STYLES))
    vector.extend(one_hot(item.get("location", ""), LOCATIONS))

    return np.array(vector)


def vectorize_input(user_input, ranges):
    vector = []

    numeric_fields = ["estimated_budget", "land_area_min", "building_area", "num_floors", "num_bedrooms", "room_area"]

    for field in numeric_fields:
        value = float(user_input.get(field, 0))
        min_val, max_val = ranges[field]
        vector.append(normalize(value, min_val, max_val))

    vector.extend(one_hot(user_input.get("style", ""), STYLES))
    vector.extend(one_hot(user_input.get("location", ""), LOCATIONS))

    return np.array(vector)
