class Client:
    def __init__ (self, id, name, contact, discount):
        self.id = id
        self.name = name
        self.contact = contact
        self.discount = discount

    def calculate_total(self, orders):
        total = sum(order.price for order in orders)
        return total * (1 - self.discount / 100)

class orders:
    def __init__(self, tipe, price):
        self.tipe = tipe
        self.price = price