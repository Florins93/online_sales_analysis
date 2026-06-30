class Product:

    def __init__(self,name,quantity,price):
        self._name = name
        self._quantity = quantity
        self._price = price

    def __str__(self):
        return f'Produsul {self._name} are pretul {self._price} si sunt disponibile ' \
        f'{self._quantity} bucati'

    def update_quantity(self, quantity):
        if isinstance(quantity, int) and quantity >= 0:
            self._quantity = quantity
        else:
            print("Cantitatea trebuie sa fie un numar intreg pozitiv.")  