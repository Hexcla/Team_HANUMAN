import numpy as np
from sklearn.neighbors import NearestNeighbors

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in kilometers
    dlat = np.radians(lat2 - lat1)
    dlon = np.radians(lon2 - lon1)
    a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(np.radians(lat1)) * np.cos(np.radians(lat2)) * np.sin(dlon/2) * np.sin(dlon/2)
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

def calculate_similarity(rider_location, driver_location):
    return haversine(rider_location[0], rider_location[1], driver_location[0], driver_location[1])

def find_best_match(rider_location, driver_locations):
    similarities = [calculate_similarity(rider_location, loc) for loc in driver_locations]
    best_match_idx = np.argmin(similarities)
    return best_match_idx, driver_locations[best_match_idx]

rider_location = (19.0760, 72.8777)  # Example coordinates (Chennai)
driver_locations = [(19.0176, 72.8562), (19.2087, 72.9780), (19.0896, 72.8656)]


best_match = find_best_match(rider_location, driver_locations)
print("Best driver match:", best_match)
