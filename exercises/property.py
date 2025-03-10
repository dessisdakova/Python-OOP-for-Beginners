class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_balue):
        self._price = new_balue

    @property
    def size(self):
        return self._price

    @size.setter
    def size(self, new_value):
        self._size = new_value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, new_value):
        self._brand = new_value

ball0 = BouncyBall(3, 6, "unknown")
ball0.price = 100
print(ball0.price)

class BouncyBall2:
    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    def get_price(self):
        return self._price

    def set_price(self, new_value):
        self._price = new_value

    def get_size(self):
        return self._size

    def set_size(self, new_value):
        self._size = new_value

    def get_brand(self):
        return self._brand

    def set_brand(self, new_value):
        self._brand = new_value

    price = property(get_price, set_price)
    size = property(get_size, set_size)
    brand = property(get_brand, set_brand)

ball =BouncyBall2(1.3, 4, "some")
print(ball.size)