# Ejercicio 3: Paquete de algoritmos de búsqueda

import controllers.search_dao as dao
import models.lineal_search as linear
import models.binary_search as binary
import os

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    search_dao = dao.SearchDAO()
    
    # Pedir datos al usuario
    print("=== PRUEBA DE BÚSQUEDA ===")
    data = list(map(int, input("Ingrese una lista de números separados por espacios: ").replace(',', ' ').split()))
    target = int(input("Ingrese el número a buscar: "))
    sorted_data = sorted(data)
    
    print(f"\nLista de numeros: {data}")
    print(f"Numero a buscar: {target}\n")
    
    # Búsqueda lineal
    print("Búsqueda Lineal:")
    res = search_dao.search('linear', data, target)
    print(f"Posición: {res}" if res != -1 else "No encontrado")
    
    # Búsqueda binaria
    print("\nBúsqueda Binaria:")
    res = search_dao.search('binary', sorted_data, target)
    print(f"Posición: {res}" if res != -1 else "No encontrado")
    
if __name__ == "__main__":
    main()
