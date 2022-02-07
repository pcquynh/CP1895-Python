from dataclasses import dataclass # Step 1: import dataclass


@dataclass
class Product:
    __price: int
    name: str
    discountPercent: int

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        assert price > 0, 'price should be greater than 0'
        self.__price = price

    def getDiscountAmount(self):
        return self.__price - self.getDiscountPrice()

    def getDiscountPrice(self):
        return (self.__price * self.discountPercent) / 100