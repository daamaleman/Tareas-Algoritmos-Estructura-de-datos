import controllers.action_controller as ac 

# Menú principal para simular historial de acciones de un editor de texto
def main():
    history = []  # Lista doblemente enlazada simulada como pila de acciones
    redo_stack = []

    while True:
        print("\n--- EDITOR DE TEXTO: HISTORIAL DE ACCIONES ---")
        print("1. Realizar acción")
        print("2. Deshacer acción")
        print("3. Rehacer acción")
        print("4. Mostrar historial")
        print("5. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            action = input("Ingrese la acción (escribir, borrar, copiar, pegar): ")
            ac.add_action(history, redo_stack, action)
        elif choice == "2":
            ac.undo_action(history, redo_stack)
        elif choice == "3":
            ac.redo_action(history, redo_stack)
        elif choice == "4":
            ac.show_history(history)
        elif choice == "5":
            print("Saliendo del historial de acciones.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
