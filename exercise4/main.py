          
import controllers.inventory_dao as dao
import os

# Clear console and set colors
os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Initialize DAO
    inventory_dao = dao.InventoryDAO()
    
    print("-" * 30)
    print("Sistema de gestión de inventario")
    print("-" * 30)
    
    # Register products
    while True:
        print("\nIngrese los datos del producto:")
        code = input("Código: ")
        name = input("Nombre: ")
        price = float(input("Precio: "))
        stock = int(input("Stock: "))
        
        product_data = {"code": code, "name": name, "price": price, "stock": stock}
        inventory_dao.register_product(product_data)
        
        another = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if another != 's':
            break
    
    # Display inventory
    print("-" * 30)
    print("\nProductos registrados:")
    print("-" * 30)
    for product in inventory_dao.get_all_products():
        print(f"- {product}")
    
    # Search example
    print("-" * 30)
    print("\nBuscar el producto:")
    print("-" * 30)
    search_code = input("Ingrese el código del producto a buscar: ")
    found = inventory_dao.search_product(search_code)
    print(f"Resultado: {found}")

if __name__ == "__main__":
    main()