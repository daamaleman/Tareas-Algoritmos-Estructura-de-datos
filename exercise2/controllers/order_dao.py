# Ejercicio 2: Módulo de ordenamiento

import models.order as mod_ord

class OrderDao:
    """DAO para manejar operaciones de ordenamiento"""
    
    def __init__(self):
        self.algorithm = mod_ord.BubbleSort()  # Acceso mediante el alias
        self.browsing = []
    
    def sort_list(self, list, ascendant=True):
        result = self.algorithm.order(list.copy(), ascendant=ascendant)
        self.browsing.append({
            'lista_original': list.copy(),
            'lista_ordenada': result,
            'ascendente': ascendant,
            'algoritmo': self.algorithm.nombre
        })
        return result
    
    def show_list(self, list, message="Lista:"):
        self.algorithm.show_list(list, message)
    