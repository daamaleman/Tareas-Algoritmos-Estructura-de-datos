
class Inventory:
    def __init__(self):
        self.products = {}
    
    def add_product(self, product):
        if product.code in self.products:
            raise ValueError("El código de producto ya existe")
        self.products[product.code] = product
    
    def find_product(self, code):
        return self.products.get(code)
    
    def remove_product(self, code):
        if code not in self.products:
            raise ValueError("Producto no encontrado")
        del self.products[code]
    
    def list_products(self):
        return list(self.products.values())