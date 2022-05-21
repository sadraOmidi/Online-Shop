import random


class Product:
    def __init__(self, name, price, count):
        self.product_code = random.randint(0, 10000)
        self.name = name
        self.price = price
        self.count = count
        self.admin_id = None
