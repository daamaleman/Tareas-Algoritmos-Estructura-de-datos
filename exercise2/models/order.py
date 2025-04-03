# Ejercicio #2: Módulo de ordenamiento Se requiere que los estudiantes diseñen un módulo independiente que contenga implementaciones de algoritmos de ordenamiento simples (bubble sort). El objetivo es que, a partir de una función principal, se invoquen los métodos del módulo para ordenar una lista de números y demostrar la correcta separación de responsabilidades, fomentando la modularidad y la reutilización del código.

class sortAlgorithm:
    """Clase base para algoritmos de ordenamiento"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def order(self, list, ascendant=True):
        raise NotImplementedError("Método abstracto")
    
    def show_list(self, list, message="Lista:"):
        print(f"{message} {', '.join(map(str, list))}")


class BubbleSort(sortAlgorithm):
    """Implementación concreta de Bubble Sort"""
    
    def __init__(self):
        super().__init__("Bubble Sort")
    
    def order(self, list, ascendant=True):
        n = len(list)
        for i in range(n):
            exchange = False
            for j in range(0, n-i-1):
                if (ascendant and list[j] > list[j+1]) or (not ascendant and list[j] < list[j+1]):
                    list[j], list[j+1] = list[j+1], list[j]
                    exchange = True
            if not exchange:
                break
        return list