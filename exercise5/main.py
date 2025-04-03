import models.client as m
import controllers.client_controllers as cc

def get_valid_int(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Por favor, ingrese un número entre {min_value} y {max_value}.")
            else:
                return value
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def get_valid_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Por favor, ingrese un número entre {min_value} y {max_value}.")
            else:
                return value
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número decimal.")

def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("La entrada no puede estar vacía. Por favor, intente de nuevo.")

def create_client(client_type):
    client_id = get_valid_int(f"Ingrese el ID para el cliente {client_type}: ", min_value=1)
    client_name = get_non_empty_string(f"Ingrese el nombre del cliente {client_type}: ")
    client_phone = get_non_empty_string(f"Ingrese el número de teléfono del cliente {client_type}: ")
    if client_type == "VIP":
        client_discount = get_valid_int("Ingrese el porcentaje de descuento para el cliente VIP: ", min_value=0, max_value=100)
    else:
        client_discount = 0  # Sin descuento para clientes regulares
    return m.Client(client_id, client_name, client_phone, client_discount)

def create_order(client_type):
    return [
        m.orders("comida", get_valid_float(f"Ingrese el precio de la comida para el cliente {client_type}: ", min_value=0)),
        m.orders("bebida", get_valid_float(f"Ingrese el precio de la bebida para el cliente {client_type}: ", min_value=0))
    ]

def main():
    regular_client = None
    vip_client = None
    regular_order = []
    vip_order = []

    while True:
        print("\nMenú:")
        print("1. Crear Cliente Regular")
        print("2. Crear Cliente VIP")
        print("3. Agregar Pedido para Cliente Regular")
        print("4. Agregar Pedido para Cliente VIP")
        print("5. Calcular Totales")
        print("6. Salir")
        choice = int(input("Ingrese su opción: ").strip())

        if choice == 1:
            regular_client = create_client("regular")
        elif choice == 2:
            vip_client = create_client("VIP")
        elif choice == 3:
            if regular_client:
                regular_order = create_order("regular")
            else:
                print("Por favor, cree un cliente regular primero.")
        elif choice == 4:
            if vip_client:
                vip_order = create_order("VIP")
            else:
                print("Por favor, cree un cliente VIP primero.")
        elif choice == 5:
            if regular_client:
                print("Total para cliente regular:", regular_client.calculate_total(regular_order))
            else:
                print("No se encontró un cliente regular.")
            if vip_client:
                print("Total para cliente VIP:", vip_client.calculate_total(vip_order))
            else:
                print("No se encontró un cliente VIP.")
        elif choice == 6:
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()