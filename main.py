from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()


manager.add_product(Product("Laptop", 5, 3500))
manager.add_product(Product("Mouse", 20, 80))
manager.add_product(Product("Tastatura", 10, 150))
manager.add_product(Product("Scaun", 1, 250))
manager.add_product(Product("Desktop", 78, 179))

print("Lista de produse:")
manager.show_products()

total = manager.show_total_value()
print(f"Valoarea totala a inventarului este: {total}")

cart = Cart()


random_products = random.sample(manager.products, 3)

for product in random_products:
    cart.add_product(product)

print("\n--- CART ---")
cart.show_cart()

print("\nTotal de plata:", cart.show_total_value())