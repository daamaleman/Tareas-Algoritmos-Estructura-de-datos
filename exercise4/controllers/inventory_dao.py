
import models.inventory as inv_model
import models.product as prod_model

class InventoryDAO:
    def __init__(self):
        self.inventory = inv_model.Inventory()
    
    def register_product(self, product_data):
        product = prod_model.Product(**product_data)
        self.inventory.add_product(product)
        return product
    
    def search_product(self, code):
        return self.inventory.find_product(code)
    
    def update_stock(self, code, amount):
        product = self.inventory.find_product(code)
        if product:
            product.update_stock(amount)
    
    def delete_product(self, code):
        self.inventory.remove_product(code)
    
    def get_all_products(self):
        return self.inventory.list_products()