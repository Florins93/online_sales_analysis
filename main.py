from product import Product
from product_manager import ProductManager

manager = ProductManager()


manager.add_product(Product("Laptop", 5, 3500))
manager.add_product(Product("Mouse", 20, 80))
manager.add_product(Product("Tastatura", 10, 150))

print("Lista de produse:")
manager.show_products()

total = manager.show_total_value()
print(f"Valoarea totala a inventarului este: {total}")