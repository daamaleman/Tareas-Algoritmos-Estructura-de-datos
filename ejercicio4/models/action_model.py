
class ActionNode:
    def __init__(self, action):
        self.action = action  # Nombre de la acción realizada
        self.prev = None  # Nodo anterior (para deshacer)
        self.next = None  # Nodo siguiente (para rehacer)
