from product import Product

class Cart:

    def __init__(self):
        self.cart_items =[]


    def add_product(self, product : Product):
        self.cart_items.append(product)

    def show_cart(self):
        if not self.cart_items:
            print("Cosul este gol.")
            return

        for product in self.cart_items:
            print(product)

    def show_total_value(self):
        if not self.cart_items:
            print("Nu există produse disponibile.")
            return

        total = 0
        for product in self.cart_items:
            total += product._quantity * product._price

        return total            
