from transportation_systems_map import transportation_systems_map
from rapidfuzz import process

def get_id_from_transportation_systems_map(transportation_system_name):
    # Use rapidFuzz to find the closest match
    match = process.extractOne(transportation_system_name, transportation_systems_map.keys())
    if match:
        return(transportation_systems_map[match[0]])
    else:
        return None
    

def serialize_without_system_field(obj):
    """
    Converts an object to a dictionary and removes the 'system' field.
    """
    serialized_obj = vars(obj)
    if "system" in serialized_obj.copy():
        del serialized_obj["system"]
    return serialized_obj