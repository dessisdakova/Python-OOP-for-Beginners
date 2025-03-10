from wsgiref.util import request_uri


class ElectronicDevices:

    def __init__(self, model: str, manufacturer: str, year: int):
        self._model = model
        self._manufacturer = manufacturer
        self._year = year

    @property
    def model(self):
        return self._model

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def year(self):
        return self._year

    def __str__(self):
        return f"Model: '{self.model}' | Manufacturer: '{self._manufacturer}' | Year: {self.year}"


class Computer(ElectronicDevices):

    def __init__(self, model: str, manufacturer: str, year: int, processor: str):
        super().__init__(model, manufacturer, year)
        self._processor = processor

    @property
    def processor(self):
        return self._processor

    def __str__(self):
        return super().__str__() + f" | Processor: '{self.processor}'"


class Tv(ElectronicDevices):

    def __init__(self, model: str, manufacturer: str, year: int, size: int):
        super().__init__(model, manufacturer, year)
        self._size = size

    @property
    def size(self):
        return self._size

    def __str__(self):
        return super().__str__() + f" | Size: {self.size} inches"

class Desktop(Computer):

    def __init__(self, model: str, manufacturer: str, year: int, processor: str, height: int, wight: int):
        super().__init__(model, manufacturer, year, processor)
        self._height = height
        self._wight = wight

    @property
    def height(self):
        return self._height

    @property
    def wight(self):
        return self._wight

    def __str__(self):
        return super().__str__() + f" | Dimensions: {self.height} x {self.wight}"

class Laptop(Computer):

    def __init__(self, model: str, manufacturer: str, year: int, processor: str, weight: float):
        super().__init__(model, manufacturer, year, processor)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return super().__str__() + f" | Weight: {self.weight} grams"

comp = Computer("A122DF", "HP", 2020, "AMD")
print(comp)

tv = Tv("LEDQD4432454FD", "LG", 2021, 55)
print(tv)

desktop  = Desktop("FD3434G", "Lenovo", 2023, "Intel", 60, 25)
print(desktop)

laptop  = Laptop("SDVF121", "Apple", 2024, "Apple M2", 1800)
print(laptop)