from products import Product


class Store:
    def __init__(self, inventory):
        for item in inventory:
            while item.name == "":
                print("Product name not entered.")
                print(f"Price: {item.price} Quantity: {item.quantity}")
                item.name = input("Please enter a product name: ").strip()

            while item.price == 0 or type(item.price) == str:
                print("Price not entered.")
                print(f"Name: {item.name} Quantity: {item.quantity}")
                try:
                    item.price = float(input("Please enter a price: "))
                except ValueError:
                    print("Enter a valid number.")

            while item.quantity == 0 or type(item.quantity) == str:
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
            if product.active == True:
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


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    Product("", price=300, quantity=500),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.inventory)
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
    for product in best_buy.get_all_products():
        print(product.name, product.price, product.quantity)


if __name__ == '__main__':
    main()