class Bubble:

    def __init__(self, size, color):
        self._size = size
        self._color = color

    def __eq__(self, other):
        return self._size == other._size and self._color == other._color

    def __gt__(self, other):
        return self._size > other._size

    def __lt__(self, other):
        return self._size < other._size

    def __ne__(self, other):
        return self._size != other._size or self._color != other._color

b1 = Bubble(1, "pink")
b2 = Bubble(1, "pink")

print(b1 != b2)


