
class Store:
    """ Defines the Store class."""
    def __init__(self, inventory):
        """ Constructs a Store object."""
        for item in inventory:
            while item.name == "":
                print("Product name not entered.")
                print(f"Price: {item.price} Quantity: {item.quantity}")
                item.name = input("Please enter a product name: ").strip()

            while item.price == 0 or isinstance(item.price, str):
                print("Price not entered.")
                print(f"Name: {item.name} Quantity: {item.quantity}")
                try:
                    item.price = float(input("Please enter a price: "))
                except ValueError:
                    print("Enter a valid number.")

            while item.quantity == 0 or isinstance(item.quantity, str):
                print("Quantity not entered.")
                print(f"Name: {item.name} Price: {item.price}")
                try:
                    item.quantity = int(input("Please enter a quantity: "))
                    break
                except ValueError:
                    print("Enter a valid number: ")

        self.inventory = inventory

    def add_product(self, product):
        """ Adds a product to the inventory."""
        self.inventory.append(product)

    def remove_product(self, product):
        """ Removes product from the inventory."""
        self.inventory.remove(product)

    def get_total_quantity(self):
        """ Gets the total number of items in the inventory."""
        total_quantity = 0
        for product in self.inventory:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """ Returns a list of all the ACTIVE products."""
        products = []
        for product in self.inventory:
            if product.active is True:
                products.append(product)
        return products

    def order(self, shopping_list):
        """ Takes a list of tuples.
            Returns the total cost of an order.
        """
        total_cost = 0.0
        for item, quantity in shopping_list:
            total_cost = item.buy(quantity)
        return total_cost
