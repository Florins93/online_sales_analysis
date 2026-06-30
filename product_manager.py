from product import Product

class ProductManager:

    def __init__(self):
        self.products = []

    def add_product(self, product : Product):
        self.products.append(product)

    def show_products(self):
        if not self.products:
            print("Nu există produse disponibile.")
            return
    
        for product in self.products:
            print(product) 

    def show_total_value(self):
        if not self.products:
            print("Nu există produse disponibile.")
            return

        total = 0
        for product in self.products:
            total += product._quantity * product._price

        return total

    def add_product_removal(self, name):
        for product in self.products:
            if name == product._name:
                self.products.remove(product)
                print(f'Produsul a fost sters!')
                return   

        print('Produsul nu exista in lista!')             

