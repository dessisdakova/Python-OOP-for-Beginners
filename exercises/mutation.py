a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c


def remove_elem(data, target):
    copy = data[:]
    for item in copy:
        if item == target:
            copy.remove(target)
    return copy


def get_product(data):
    total = 1
    copy = data[:]
    for i in range(len(copy)):
        total *= copy.pop()
    return total

remove_elem(c, 3)
print(get_product(b))
print(a)