class Product:
    def __init__(self, name, price, quantity):
        """ Constructs Product object."""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """ Returns the remaining quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """ Sets the quantity of the product."""
        self.quantity = quantity
        if quantity <= 0:
            self.deactivate()

    def is_active(self):
        """ Returns True if the product is active."""
        return self.active

    def activate(self):
        """ Sets the product.active to True."""
        self.active = True

    def deactivate(self):
        """ Sets the product.active to False."""
        self.active = False

    def show(self):
        """ Displays the product information."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """ Processes an order.
            Checks if there is enough in the inventory.
            Calculates the price for the order.
            Removes the ordered items from inventory.
            Returns the total price
        """
        try:
            if self.quantity < quantity:
                raise ValueError("Not enough product to fulfill order!")
        except ValueError as ve:
            return ve
        else:
            total_price = self.price * quantity
            remaining_quantity = self.quantity - quantity
            self.set_quantity(remaining_quantity)
            return float(total_price)
