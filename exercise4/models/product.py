
class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, amount):
        if self.stock + amount < 0:
            raise ValueError("No se puede tener stock negativo")
        self.stock += amount
    
    def update_price(self, new_price):
        if new_price <= 0:
            raise ValueError("El precio debe ser positivo")
        self.price = new_price
    
    def __str__(self):
        return f"{self.code} - {self.name} (${self.price:.2f}) | Stock: {self.stock}"