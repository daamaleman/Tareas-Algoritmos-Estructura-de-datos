import controllers.route_controller  as rc

# Menú principal para interactuar con el usuario
def main():
    route = rc.create_route()

    print("\n--- MAPA DE RUTA ---")
    start = input("Ingrese la estación de origen: ")
    end = input("Ingrese la estación de destino: ")

    result = rc.estimate_route_time(route, start, end)
    print(result)

if __name__ == "__main__":
    main()
