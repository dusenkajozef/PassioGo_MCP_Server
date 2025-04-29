import passiogo

def get_routes_from_transportation_system_id(transportation_system_id):
    return passiogo.getSystemFromID(transportation_system_id).getRoutes()


def get_stops_from_transportation_system_id(transportation_system_id):
    return passiogo.getSystemFromID(transportation_system_id).getStops()


def get_alerts_from_transportation_system_id(transportation_system_id):
    return passiogo.getSystemFromID(transportation_system_id).getSystemAlerts()


def get_vehicles_from_transportation_system_id(transportation_system_id):
    return passiogo.getSystemFromID(transportation_system_id).getVehicles()