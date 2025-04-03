import controllers.order_dao as dao
import models.order as mod_ord
import os

# Limpiar consola y configurar colores
os.system('cls' if os.name == 'nt' else 'clear')

# Crear instancia del DAO
order_dao = dao.OrderDao()

# Pedir al usuario que ingrese una lista de números
enter = input("Ingrese una lista de números separados por comas: ")
numbers = list(map(int, enter.split(',')))

# Mostrar lista original
order_dao.show_list(numbers, "Lista original:")

# Ordenar ascendente
ascendant = order_dao.sort_list(numbers)
order_dao.show_list(ascendant, "Orden ascendente:")

# Ordenar descendente
descending = order_dao.sort_list(numbers, ascendant=False)
order_dao.show_list(descending, "Orden descendente:")