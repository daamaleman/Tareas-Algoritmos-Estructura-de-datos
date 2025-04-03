class Invoice:
    def __init__(self, product_name, quantity, price, discount):
        self.product_name = product_name
        self.quantity = quantity
        self.price = price
        self.discount = discount
    
    def calculate_total(self):
        if self.validations():
            raise ValueError("Datos invalidos")
        else:
            return self.price * self.quantity * (1 - self.discount)
    
    def generate_report(self):
        return (
        f"Producto: {self.product_name}\n"
        f"quantity: {self.quantity}\n"
        f"price: {self.price:.2f}\n"
        f"discount: {self.discount * 100:.2f}\n"
        f"Total: {self.calculate_total():.2f}\n" )

    def validations(self):
        if self.product_name is not str(self.product_name):
            return "Error: El nombre del producto debe ser una cadena de texto."
        if self.quantity is not int(self.quantity):
            return "Error: La quantity debe ser un número entero."
        if self.price is not float(self.price):
            return "Error: El price debe ser un número decimal."
        if self.discount is not float(self.discount):
            return "Error: El discount debe ser un número decimal."
        
        