class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, estudiante):
        nuevo = Nodo(estudiante)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def obtener_lista(self):
        actual = self.cabeza
        lista = []
        while actual:
            lista.append(actual.estudiante)
            actual = actual.siguiente
        return lista

    def ordenar_por(self, campo):
        lista = self.obtener_lista()
        lista.sort(key=lambda est: getattr(est, campo))
        nueva_lista = ListaEnlazada()
        for estudiante in lista:
            nueva_lista.agregar(estudiante)
        return nueva_lista
