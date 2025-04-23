import models.route_model as rm

# Crea una ruta de estaciones predefinida
def create_route():
    route = rm.RouteMap()
    route.add_station("Estación A", 5)
    route.add_station("Estación B", 7)
    route.add_station("Estación C", 3)
    route.add_station("Estación D", 4)
    return route

# Calcula el tiempo estimado entre dos estaciones dadas
def estimate_route_time(route, start, end):
    return route.estimate_time(start, end)
