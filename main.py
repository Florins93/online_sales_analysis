from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()


manager.add_product(Product("Casa", 5, 3500))
manager.add_product(Product("Masina", 20, 80))
manager.add_product(Product("Canapea", 10, 150))
manager.add_product(Product("Scaun", 1, 250))
manager.add_product(Product("Desktop", 78, 179))



cart = Cart()


random_products = random.sample(manager.products, 3)

for product in random_products:
    cart.add_product(product)

print("\n--- CART ---")
cart.show_cart()

print("\nTotal de plata:", cart.show_total_value())