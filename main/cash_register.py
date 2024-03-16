# cash_register.py

class CashRegister:
    def __init__(self):
        self.items = {}
        self.prices = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
            self.prices[item] = price

    def calculate_total(self):
        return sum(
            self.prices[item] * quantity for item, quantity in self.items.items()
        )

    def apply_discount(self, item, discount):
        if item in self.prices:
            self.prices[item] -= discount
        else:
            raise ValueError("Item not found")
