import asyncio
import os
#from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP
from rapidfuzz import process
from passiogo_client import get_routes_from_transportation_system_id, get_stops_from_transportation_system_id, get_alerts_from_transportation_system_id, get_vehicles_from_transportation_system_id
from core_utils import get_id_from_transportation_systems_map, serialize_without_system_field


mcp = FastMCP("passiogo-mcp-server")
USER_AGENT = "passiogo-agent/1.0"


@mcp.tool()
def get_routes_from_transportation_system(transportation_system_name: str):
    """
    Finds the informations about the routes of a transportation system by its name.

    Args:
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').

    Returns:
        A list of dictionaries containing the information about the routes.
    """
    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")
    routes = get_routes_from_transportation_system_id(transportation_system_id)
    if not routes:
        raise ValueError(f"No routes found for transportation system ID '{transportation_system_id}'.")
    
    serializable_routes = [serialize_without_system_field(route) for route in routes]
    return serializable_routes


@mcp.tool()
def get_route_from_transportation_system(transportation_system_name: str, route_name: str):
    """
    Finds the information about a route by its name and the transportation system name.

    Args:
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').
        route_name: The approximate name of the route (e.g., 'Tech Trolley', 'Red Route').

    Returns:
        A dictionary containing the information about the route.
    """
    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")
    
    routes = get_routes_from_transportation_system_id(transportation_system_id)
    if not routes:
        raise ValueError(f"No routes found for transportation system ID '{transportation_system_id}'.")
    
    # Use rapidFuzz to find the closest match
    route_match = process.extractOne(route_name, [route.name for route in routes])
    if route_match:
        route = routes[route_match[2]]
    else:
        raise ValueError(f"Route '{route_name}' not found in transportation system ID '{transportation_system_id}'.")
    
    route_dict = serialize_without_system_field(route)
    return route_dict


@mcp.tool()
def get_stops_from_transportation_system(transportation_system_name: str):
    """
    Finds the informations about the stops of a transportation system by its name.

    Args:
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').

    Returns:
        A list of dictionaries containing the information about the stops.
    """
    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")
    stops = get_stops_from_transportation_system_id(transportation_system_id)
    if not stops:
        raise ValueError(f"No stops found for transportation system ID '{transportation_system_id}'.")
    
    serializable_stops = [serialize_without_system_field(stop) for stop in stops]
    return serializable_stops


@mcp.tool()
def get_stop_from_transportation_system(stop_name: str, transportation_system_name: str):
    """
    Finds the information about a stop by its name, and transportation system name.

    Args:
        stop_name: The approximate name of the stop (e.g., 'Tech Square', 'Student Center').
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').

    Returns:
        A dictionary containing the information about the stop.
    """
    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")

    stops = get_stops_from_transportation_system_id(transportation_system_id)
    if not stops:
        raise ValueError(f"No stops found for transportation system ID '{transportation_system_id}'.")
    
    # Use rapidFuzz to find the closest match
    stop_match = process.extractOne(stop_name, [stop.name for stop in stops])
    if stop_match:
        stop = stops[stop_match[2]]
    else:
        raise ValueError(f"Stop '{stop_name}' not found in transportation system ID '{transportation_system_id}'.")

    stop_dict = serialize_without_system_field(stop)
    return stop_dict


@mcp.tool()
def get_stops_from_route(route_name: str, transportation_system_name: str):
    """
    Finds the informations about the stops of a route by its name and the transportation system name.
    Args:
        route_name: The approximate name of the route (e.g., 'Tech Trolley', 'Red Route').
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').
    Returns:
        A list of dictionaries containing the information about the stops.
    """
    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")
    
    routes = get_routes_from_transportation_system_id(transportation_system_id)
    if not routes:
        raise ValueError(f"No routes found for transportation system ID '{transportation_system_id}'.")
    
    # Use rapidFuzz to find the closest match
    route_match = process.extractOne(route_name, [route.name for route in routes])
    if route_match:
        route = routes[route_match[2]]
    else:
        raise ValueError(f"Route '{route_name}' not found in transportation system ID '{transportation_system_id}'.")
    
    stops = route.getStops()
    if not stops:
        raise ValueError(f"No stops found for route ID '{route.id}' in transportation system ID '{transportation_system_id}'.")
    
    serializable_stops = [serialize_without_system_field(stop) for stop in stops]
    return serializable_stops


@mcp.tool()
def get_alerts_from_transportation_system(transportation_system_name: str):
    """
    Finds the alerts of a transportation system by its name.
    Args:
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').
    Returns:
        A list of dictionaries containing the information about the alerts.
    """

    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")
    
    alerts = get_alerts_from_transportation_system_id(transportation_system_id)
    if not alerts:
        raise ValueError(f"No alerts found for transportation system ID '{transportation_system_id}'.")
    
    serializable_alerts = [serialize_without_system_field(alert) for alert in alerts]
    return serializable_alerts


@mcp.tool()
def get_vehicles_from_transportation_system(transportation_system_name: str):
    """
    Finds the vehicles of a transportation system by its name.
    Args:
        transportation_system_name: The approximate name of the transportation system (e.g., 'Georgia Tec', 'University of Arkansas', 'West Midtown Shuttle').
    Returns:
        A list of dictionaries containing the information about the vehicles.
    """
    transportation_system_id = get_id_from_transportation_systems_map(transportation_system_name)
    if not transportation_system_id:
        raise ValueError(f"Transportation system '{transportation_system_name}' not found.")
    
    vehicles = get_vehicles_from_transportation_system_id(transportation_system_id)
    if not vehicles:
        raise ValueError(f"No vehicles found for transportation system ID '{transportation_system_id}'.")

    serializable_vehicles = [serialize_without_system_field(vehicle) for vehicle in vehicles]
    return serializable_vehicles


'''def main():
    print("Hello from passiogo-mcp-server!")
    print(f"Loaded {len(transportation_systems_map)} transportation systems.")
    approximate_transportation_system_name = "University of Arkansas"

    vehicles = get_vehicles_from_transportation_system(approximate_transportation_system_name)
    print(vehicles)'''


if __name__ == "__main__":
    #main()
    #mcp.run(transport="stdio") This was for local server

    # Fetch the port from environment variables (default to 8888 if not set)
    port = int(os.environ.get("PORT", 3152))
    
    '''# Start the server asynchronously
    asyncio.run(
        mcp.run_sse_async(
            host="0.0.0.0",  # Expose on all network interfaces
            port=port,  # Port for remote access (or local)
            log_level="debug"  # Enable debug-level logging
        )
    )'''

    mcp.run(
    transport="sse",
    host="0.0.0.0",
    port=port,
    log_level="debug"
    )