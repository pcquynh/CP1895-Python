class Product:
    def __init__(self, name: str, price: float, discount_percent: int ):
        self.name = name
        self.price = price
        self.discount_percent = discount_percent

    def get_discount_amount(self):
        return round(self.price * self.discount_percent/100, 2)

    def get_discount_price(self):
        return round(self.price - self.get_discount_amount(), 2)

    def display_info(self):
        print(f"This product has name {self.name} and price of {self.price}$.")
        print(f"This product has discount of {self.discount_percent}%.")
        print(f"The discount amount is {self.get_discount_amount()}$.")
        print(f"The price after discount is {self.get_discount_price()}$.")


product1 = Product('Stanley 13 Ounce Wood Hammer', 12.99, 62)
product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0)
product1.display_info()
print()
product2.display_info()


