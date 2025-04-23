from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from transportation_systems_map import transportation_systems_map
from rapidfuzz import process
import passiogo

load_dotenv()

mcp = FastMCP("passiogo-mcp-server")

USER_AGENT = "passiogo-agent/1.0"


def get_id_from_transportation_systems_map(transportation_system_name):
    # Use rapidFuzz to find the closest match
    match = process.extractOne(transportation_system_name, transportation_systems_map.keys())
    if match:
        return(transportation_systems_map[match[0]])
    else:
        return None
    

def get_routes_from_transportation_system_id(transportation_system_id):
    return passiogo.getSystemFromID(transportation_system_id).getRoutes()


def get_stops_from_transportation_system_id(transportation_system_id):
    return passiogo.getSystemFromID(transportation_system_id).getStops()


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
    
    serializable_routes = []
    for route in routes:
        route_dict = vars(route)
        # Remove non-serializable attributes
        if "system" in route_dict:
            del route_dict["system"]        
        serializable_routes.append(route_dict)

    return serializable_routes

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
    
    serializable_stops = []
    for stop in stops:
        stop_dict = vars(stop)
        # Remove non-serializable attributes
        if "system" in stop_dict:
            del stop_dict["system"]        
        serializable_stops.append(stop_dict)
    return serializable_stops


'''def main():
    print("Hello from passiogo-mcp-server!")
    print(f"Loaded {len(transportation_systems_map)} transportation systems.")
    approximate_name = input("Enter an approximate name: ")
    routes = get_stops_from_transportation_system(approximate_name)
    print(routes)'''


if __name__ == "__main__":
    #main()
    mcp.run(transport="stdio")