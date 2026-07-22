import sys

import products
import store


def start(best_buy):
    """
    Displays the main menu
    :param best_buy: Store object
    :return:
    """

    print("\n-------------------")
    print("Menu")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make order")
    print("4. Quit")


def get_action():
    """ Get an action choice from the user."""
    while True:
        try:
            action = int(input("Please choose a number: "))
            if action not in action_dictionary:
                raise ValueError("Please enter a valid number.")
            return action

        except ValueError:
            print("Please enter a valid number.")


def list_all_products(best_buy):
    """ Prints a list of all the active products"""
    inventory_list = best_buy.get_all_products()
    product_count = 0
    print("-------------------\n")
    for product in inventory_list:
        product_count += 1
        print(f"{product_count}. ", end="")
        product.show()
    return inventory_list


def total_items_in_store(best_buy):
    """ Displays the total number of items in inventory."""
    total_inventory = best_buy.get_total_quantity()
    print("-------------------\n")
    print(f"There are {total_inventory} items in store.")


def make_order(best_buy):
    """ Prompts user to select items and quantities to buy.
        Displays the payment due.
    """
    inventory_list = best_buy.get_all_products()
    shopping_list = []
    item = ""
    quantity = 0

    print("When the order is complete, enter 0.")
    # Select product
    while True:
        while True:
            try:
                item_num = int(input("Which product # would you like: "))
                if item_num == 0:
                    break
                if item_num not in range(len(inventory_list) + 1):
                    raise ValueError("Please enter a valid product #.")
                item = inventory_list[item_num - 1]
                print(item.name)
                break
            except ValueError:
                print("Please enter a valid number.")

        # Enter amount
        while True:
            if item_num == 0:
                break
            try:
                quantity = int(input("How many would you like: "))
                if quantity > item.get_quantity():
                    print("Not enough in stock. There are only "
                          f"{item.get_quantity()} available.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number.")
        if item_num > 0:
            shopping_list.append((item, quantity))
            print("Item added to list!")
        else:
            print("********")
            total_cost = best_buy.order(shopping_list)
            print(f"Order made! Total payment due: ${total_cost:.2f}")
            break

def quit_app(best_buy):
    print("\n-------------------")
    print("Thanks for using BestBuy. Goodbye!")
    sys.exit()


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

# setup app actions dictionary
action_dictionary = {
    1: list_all_products,
    2: total_items_in_store,
    3: make_order,
    4: quit_app
}


def main():
    print("Welcome to BestBuy!")
    while True:
        start(best_buy)
        action = get_action()
        action_dictionary[action](best_buy)






if __name__ == '__main__':
    main()