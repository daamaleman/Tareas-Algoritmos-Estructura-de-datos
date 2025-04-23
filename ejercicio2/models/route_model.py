
class StationNode:
    def __init__(self, name, time_to_next):
        self.name = name  # Nombre de la estación
        self.time_to_next = time_to_next  # Tiempo a la siguiente estación
        self.next = None  # Referencia a la siguiente estación

class RouteMap:
    def __init__(self):
        self.head = None  # Nodo inicial de la ruta

    def add_station(self, name, time_to_next):
        # Añade una nueva estación al final de la lista
        new_node = StationNode(name, time_to_next)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def estimate_time(self, start, end):
        # Calcula el tiempo entre dos estaciones
        current = self.head
        total_time = 0
        found_start = False

        while current:
            if current.name == start:
                found_start = True
            if found_start:
                if current.name == end:
                    return f"Tiempo estimado de '{start}' a '{end}': {total_time} minutos."
                total_time += current.time_to_next
            current = current.next

        return "Ruta inválida o estaciones no encontradas."
