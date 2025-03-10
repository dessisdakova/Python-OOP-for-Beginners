class CashRegister:

    def __init__(self, cashier_name):
        self._cashier_name = cashier_name
        self._products = {}

    @property
    def cashier_name(self):
        return self._cashier_name

    @property
    def products(self):
        return self._products

    def add_product(self, product: dict, count=1):
        product_name = product["name"]
        product_price =  product["price"] * count
        self.products[product_name] = product_price

    def show_current_products(self):
        if self.products:
            for product, price in self.products.items():
                print(f"Product: {product}, price: {price}")
        else:
            print("No products adde to purchases.")

    def remove_product(self, product_name: str):
        if product_name.capitalize() in self.products.keys():
            del self.products[product_name]
        else:
            print(f"No '{product_name}' in purchases!")

    def update_product_price(self, product_name: str, new_price: float):
        if product_name.capitalize() in self.products.keys():
            self.products[product_name] = new_price
        else:
            print(f"No '{product_name}' in purchases!")

    def calculate_subtotal_no_tax(self):
        subtotal = 0
        for price in self.products.values():
            subtotal += price
        return subtotal

    def calculate_tax(self):
        subtotal = self.calculate_subtotal_no_tax()
        return subtotal * 0.05

    def calculate_total(self):
        return f"{self.calculate_subtotal_no_tax() + self.calculate_tax():.2f}"

    def clear(self):
        self.products.clear()


product1 = {"name": "Pizza", "price": 10.34}
product2 = {"name": "Brownie", "price": 4.99}
product3 = {"name": "Sandwich", "price": 8.50}
product4 = {"name": "Chocolate", "price": 2.35}

cash = CashRegister("Mike")
cash.add_product(product1, 2)
cash.add_product(product4)
cash.show_current_products()
# print(cash.calculate_subtotal_no_tax())
print(cash.calculate_total())
cash.clear()
cash.show_current_products()
print(cash.calculate_total())