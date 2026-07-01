# Online Sales Analysis Project

## Description
This project is a simple Python application that simulates an online sales system.  
It is built using object-oriented programming (OOP) principles and demonstrates how different classes interact to manage products and a shopping cart.

---

## Project Structure

- `product.py` – Defines the Product class
- `product_manager.py` – Manages a collection of products
- `cart.py` – Handles shopping cart operations
- `main.py` – Entry point of the application
- `config.json` – Configuration file
- `screenshots/` – Folder used for documentation images (ignored by Git)

---

## Class Descriptions

### Product
Represents a single product in the system.  
It stores basic information such as name, quantity, and price.  
It also includes methods to update product quantity and format how the product is displayed.

---

### ProductManager
Responsible for managing a list of products.  
It allows adding new products, removing products by name, displaying all available products, and calculating the total value of all products in the system.

---

### Cart
Represents a shopping cart that stores selected products.  
It allows adding products to the cart, displaying cart contents, and calculating the total price of all items in the cart.

---

## Notes
- The `config.json` file contains sample configuration data used for testing.
- The `screenshots/` folder is excluded from version control using `.gitignore`.
- The project is intended for learning and practicing OOP concepts in Python.