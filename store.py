from products import Product


class Store:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product):
        self.inventory.append(product)

    def remove_product(self, product):
        self.inventory.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.inventory:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        products = []
        for product in self.inventory:
            if product.active == True:
                products.append(product)
        return products

    def order(self, shopping_list):
        total_cost = 0.0
        for item, quantity in shopping_list:
            total_cost = total_cost + (item.price * quantity)
        return total_cost


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))


if __name__ == '__main__':
    main()