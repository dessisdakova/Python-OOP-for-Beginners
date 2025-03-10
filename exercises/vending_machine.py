class VendingMachine:
    total_revenue = 0  # Total revenue of all vending machines in the system

    snack_prices = {"candy": 2.00, "soda": 1.50, "chips": 3.00, "cookies": 3.50}

    def __init__(self, inventory, serial, days_until_maintenance):
        self.inventory = inventory
        self.revenue = 0
        self.serial = serial
        self.days_until_maintenance = days_until_maintenance

    def sales_menu(self):

        while True:

            greetings = "\nWelcome! I have:\n"
            request = "\nPlease enter the number of the item: "

            print(greetings)

            i = 1
            for snack in self.inventory:
                print("(" + str(i) + ") " + snack.capitalize())
                i += 1

            cust_input = int(input(request))

            while cust_input <= 0 or cust_input > len(self.inventory):
                print("Please enter a number from 1 to", len(self.inventory))
                cust_input = int(input(request))

            self.process_sale(list(self.inventory.keys())[cust_input - 1].lower())
            answer = int(input("\nWould you like to buy another snack?\nEnter 1 for YES and 0 for NO: "))

            if not answer:
                break

    def process_sale(self, option):  # option must be in lowercase

        print("\nYou selected: %s" % option.capitalize())

        if self.inventory[option] > 0:

            print("Great! I currently have %d %s in my inventory\n" % (self.inventory[option], option))

            num_items = int(input("How many %s would you like to buy?\n" % option))

            while num_items <= 0:
                print("Please enter a positive integer")
                num_items = int(input("\nHow many %s would you like to buy?\n" % option))

            if num_items <= self.inventory[option]:
                self.remove_from_inventory(option, num_items)

                total = self.update_revenue(option, num_items)

                print("That would be: $ " + str(total))

                print("\nThank you for your purchase!")
                print("Now I have %d %s and my revenue is $%d" % (self.inventory[option], option, self.revenue))

            else:
                print("I don't have so many %s. Sorry! :(" % option)

        else:
            print("I don't have any more %s. Sorry! :(" % option)

    def remove_from_inventory(self, option, num_items):
        self.inventory[option] -= num_items

    def update_revenue(self, option, num_items):
        # Find price of the snack
        price = self.find_snack_price(option)

        # Update Instance and class
        self.revenue += num_items * price
        VendingMachine.total_revenue += num_items * price

        return num_items * price

    def find_snack_price(self, snack):
        return VendingMachine.snack_prices[snack]

    def display_revenue(self):
        print("The total revenue of this vending machine is:", self.revenue)


class HospitalVendingMachine(VendingMachine):

    snack_prices = {"candy": 2.20, "soda": 1.70, "chips": 3.20, "cookies": 3.70}

    def sales_menu(self):
        print("Welcome to our Hospital Vending Machine")
        print("We hope you are feeling better today!")
        super().sales_menu()

    def find_snack_price(self, snack):
        return HospitalVendingMachine.snack_prices[snack]

    def print_days_until_maintenance(self):
        print(f"{self.days_until_maintenance} day until maintenance.")


class SchoolVendingMachine(VendingMachine):

    snack_prices = {"candy": 1.80, "soda": 1.30, "chips": 2.80, "cookies": 3.30}
    student_debt = {"Charlie": 2.60, "Bella": 1.80, "Mike": 4.60}

    def sales_menu(self):
        print("Welcome to our School Vending Machine")
        print("We hope you have a great day full of learning!")
        super().sales_menu()

    def find_snack_price(self, snack):
        return SchoolVendingMachine.snack_prices[snack]

    def print_student_debt(self, student_name):
        if student_name in SchoolVendingMachine.student_debt.keys():
            print(f"{student_name} owes {SchoolVendingMachine.student_debt[student_name]} dollars.")
        else:
            print(f"{student_name} doesn't owe any money.")


floor_machine = VendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "011423424", 24)
# floor_machine.sales_menu()

hospital_machine = HospitalVendingMachine({"candy": 32, "soda": 50, "chips": 45, "cookies": 80}, "03223424", 15)
# hospital_machine.sales_menu()
# hospital_machine.print_days_until_maintenance()

school_machine = SchoolVendingMachine({"candy": 36, "soda": 15, "chips": 40, "cookies": 120}, "0534424", 2)
# school_machine.sales_menu()
# school_machine.print_student_debt("Jessie")
# school_machine.print_student_debt("Mike")