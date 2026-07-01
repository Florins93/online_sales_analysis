from product import Product
from product_manager import ProductManager

manager = ProductManager()


manager.add_product(Product("Casa", 5, 3500))
manager.add_product(Product("Masina", 20, 80))
manager.add_product(Product("Canapea", 10, 150))

