menu = {
    "Americano": 100,
    "Latte": 150,
    "Cappuccino": 200,
    "Espresso": 120,
    "Mocha": 180
}


def show_menu():
    print("\n~ ~ ~ COFFEE MENU ~ ~ ~")

    for coffee, price in menu.items():
        print(coffee, "₹", price)


def coffee_order():
    while True:
        order = input("\nWhat coffee would you like to order? ").title()

        if order in menu:
            print("You selected:", order)
            return order

        else:
            print("Sorry, we don't have that coffee on the menu.")


def milk_selection():
    milk = input("""
Choose your milk:

1. Regular
2. Oat (+₹20)
3. Almond (+₹30)

Enter your choice:
""")

    if milk == "1":
        milk_name = "Regular"
        milk_price = 0

    elif milk == "2":
        milk_name = "Oat"
        milk_price = 20

    elif milk == "3":
        milk_name = "Almond"
        milk_price = 30

    else:
        print("Invalid milk choice. Regular milk selected.")
        milk_name = "Regular"
        milk_price = 0

    return milk_name, milk_price


def size_selection():
    size = input("""
Choose your size:

1. Small
2. Medium (+₹30)
3. Large (+₹50)

Enter your choice:
""")

    if size == "1":
        size_name = "Small"
        size_price = 0

    elif size == "2":
        size_name = "Medium"
        size_price = 30

    elif size == "3":
        size_name = "Large"
        size_price = 50

    else:
        print("Invalid size choice. Defaulting to Small.")
        size_name = "Small"
        size_price = 0

    return size_name, size_price


def get_quantity():
    while True:
        try:
            quantity = int(
                input("\nHow many cups would you like? ")
            )

            if quantity > 0:
                return quantity

            print("Quantity must be greater than 0. Please try again.")

        except ValueError:
            print("Please enter a valid number.")


def order_type_selection():
    order_type = input("""
Choose order type:

1. For here
2. To go

Enter your choice:
""")

    if order_type == "1":
        return "For here"

    elif order_type == "2":
        return "To go"

    else:
        print("Invalid order type. Defaulting to For here.")
        return "For here"


def calculate_total(order, milk_price, size_price, quantity):
    coffee_price = menu[order]
    total = (coffee_price + milk_price + size_price) * quantity

    return total


def add_to_cart(cart, order, milk_name, size_name,
                quantity, order_type, total):

    cart.append({
        "coffee": order,
        "milk": milk_name,
        "size": size_name,
        "quantity": quantity,
        "order_type": order_type,
        "total": total
    })


def show_cart(cart):
    print("\n~ ~ ~ CURRENT ORDER ~ ~ ~")

    for index, item in enumerate(cart, start=1):
        print(
            index,
            ".",
            item["coffee"],
            "-",
            item["size"],
            "-",
            item["milk"],
            "- ₹",
            item["total"]
        )


def remove_order(cart):
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    show_cart(cart)

    while True:
        try:
            remove = int(
                input("\nWhich order would you like to remove? ")
            )

            if 1 <= remove <= len(cart):
                removed_item = cart.pop(remove - 1)

                print(
                    removed_item["coffee"],
                    "has been removed from your order."
                )

                break

            else:
                print(
                    "Invalid order number. "
                    "Please choose a number from the list."
                )

        except ValueError:
            print("Please enter a valid number.")


def final_summary(cart):
    print("\n~ ~ ~ YOUR ORDER ~ ~ ~")

    grand_total = 0

    if len(cart) == 0:
        print("Your cart is empty.")

    else:
        for index, item in enumerate(cart, start=1):
            print("\nItem", index)
            print("Coffee:", item["coffee"])
            print("Milk:", item["milk"])
            print("Size:", item["size"])
            print("Quantity:", item["quantity"])
            print("Order Type:", item["order_type"])
            print("Item Total: ₹", item["total"])

            grand_total += item["total"]

        print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
        print("GRAND TOTAL: ₹", grand_total)


print("\n~ ~ ~ WELCOME TO THE COFFEE SHOP ~ ~ ~")

cart = []

show_menu()


while True:

    # Coffee selection
    order = coffee_order()

    # Milk selection
    milk_name, milk_price = milk_selection()

    # Size selection
    size_name, size_price = size_selection()

    # Quantity
    quantity = get_quantity()

    # Order type
    order_type = order_type_selection()

    # Calculate price
    total = calculate_total(
        order,
        milk_price,
        size_price,
        quantity
    )

    # Add order to cart
    add_to_cart(
        cart,
        order,
        milk_name,
        size_name,
        quantity,
        order_type,
        total
    )

    print("\nAdded to your order!")
    print("Current item total: ₹", total)

    # Ask what the customer wants to do next
    while True:

        print("""
What would you like to do?

1. Order another coffee
2. Remove an order
3. Finish order
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            break

        elif choice == "2":
            remove_order(cart)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if choice == "3":
        break


final_summary(cart)

print("\nThank you for visiting! Enjoy your coffee!")