#Ejercicio 3: Paquete de algoritmos de búsqueda

import models.lineal_search as lineal
import models.binary_search as binary

class SearchDAO:
    def __init__(self):
        self.algorithms = {
            'linear': lineal.LinealSearch(),
            'binary': binary.BinarySearch()
        }
        self.history = []
    
    def search(self, algo_type, data, target):
        algo = self.algorithms.get(algo_type)
        if not algo:
            raise ValueError("Algoritmo no existe")
        
        result = algo.search(data, target)
        self.history.append({
            'algo': algo.get_name(),
            'target': target,
            'result': result
        })
        return result