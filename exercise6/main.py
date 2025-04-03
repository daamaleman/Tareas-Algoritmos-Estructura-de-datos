import models.invoice as mi

def request_data():
    while True:
        try:
            description = input("Ingrese la descripción del producto: ").strip()
            if not description:
                raise ValueError("La descripción no puede estar vacía.")
            
            quantity = int(input("Ingrese la cantidad: ").strip())
            if quantity <= 0:
                raise ValueError("La cantidad debe ser un número entero positivo.")
            
            unit_price = float(input("Ingrese el precio unitario: ").strip())
            if unit_price <= 0:
                raise ValueError("El precio unitario debe ser un número decimal positivo.")
            
            tax = float(input("Ingrese el impuesto (0-1): ").strip())
            if not (0 <= tax <= 1):
                raise ValueError("El impuesto debe ser un número decimal entre 0 y 1.")
            
            return description, quantity, unit_price, tax
        except ValueError as e:
            print(f"Error: {e}. Por favor, intente de nuevo.")
        except Exception as e:
            print(f"Error inesperado: {e}. Por favor, intente de nuevo.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Generar factura")
        print("2. Salir")
        option = input("Ingrese una opción: ").strip()
        
        if option == "1":
            try:
                description, quantity, unit_price, tax = request_data()
                invoice = mi.Invoice(description, quantity, unit_price, tax)
                
                total = invoice.calculate_total()
                print(f"\nEl total de la venta es: {total:.2f}")
                
                report = invoice.generate_report()
                print(f"El reporte de la factura es:\n{report}")
            except AttributeError:
                print("Error: La clase 'Invoice' no tiene los métodos necesarios.")
            except Exception as e:
                print(f"Error inesperado: {e}.")
        elif option == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu()