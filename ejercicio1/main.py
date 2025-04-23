import controllers.studentDao  as dao

def menu():
    lista = None
    while True:
        print("\n--- MENÚ ---")
        print("1. Generar estudiantes al azar")
        print("2. Mostrar estudiantes")
        print("3. Ordenar estudiantes por campo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("¿Cuántos estudiantes desea generar? "))
            lista = dao.generar_estudiantes(n)
            print("Estudiantes generados con éxito.")
        elif opcion == "2":
            if lista:
                dao.mostrar_lista(lista)
            else:
                print("Primero debe generar la lista.")
        elif opcion == "3":
            if lista:
                campo = input("Ingrese el campo por el que desea ordenar (carnet, nombres, apellidos, peso, estatura, sexo, promedio): ")
                if hasattr(lista.cabeza.estudiante, campo):
                    lista = lista.ordenar_por(campo)
                    print("Lista ordenada por", campo)
                else:
                    print("Campo no válido.")
            else:
                print("Primero debe generar la lista.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
