import controllers.patient_controller as pc

# Menú principal para gestionar la cola de pacientes
def main():
    clinic_queue = []  # Lista para manejar pacientes en orden de llegada

    while True:
        print("\n--- SISTEMA DE RECEPCIÓN DE CLÍNICA ---")
        print("1. Ingresar nuevo paciente")
        print("2. Mostrar lista de pacientes")
        print("3. Atender al siguiente paciente")
        print("4. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            name = input("Nombre completo del paciente: ")
            try:
                age = int(input("Edad del paciente: "))
                if age <= 0:
                    print("La edad debe ser un número positivo.")
                    continue
            except ValueError:
                print("Edad inválida. Debe ingresar un número.")
                continue
            symptom = input("Síntoma principal: ")
            try:
                priority = int(input("Prioridad (1 a 5): "))
                if not 1 <= priority <= 5:
                    print("La prioridad debe estar entre 1 y 5.")
                    continue
            except ValueError:
                print("Prioridad inválida. Debe ser un número entre 1 y 5.")
                continue
            
            pc.add_patient(clinic_queue, name, age, symptom, priority)
            print("Paciente agregado exitosamente.")

        elif option == "2":
            pc.show_queue(clinic_queue)

        elif option == "3":
            pc.attend_patient(clinic_queue)

        elif option == "4":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
