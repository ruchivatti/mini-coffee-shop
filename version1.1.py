menu = {
    "Americano": 100,
    "Latte": 150,
    "Cappuccino": 200,
    "Espresso": 120,
    "Mocha": 180
}

print("\n~ ~ ~ WELCOME TO THE COFFEE SHOP ~ ~ ~")

print("\n~ ~ ~ COFFEE MENU ~ ~ ~")

for coffee, price in menu.items():
    print(coffee, "₹", price)

cart = []

while True:

    # Coffee selection
    order = input("\nWhat coffee would you like to order? ").title()

    if order not in menu:
        print("Sorry, we don't have that coffee on the menu.")
        continue

    print("You selected:", order)

    # Milk selection
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

    # Size selection
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

    # Quantity
    while True:

        try:
            quantity = int(
                input("\nHow many cups would you like? ")
            )

            if quantity > 0:
                break

            print("Quantity must be greater than 0. Please try again.")

        except ValueError:
            print("Please enter a valid number.")

    # Order type
    order_type = input("""
Choose order type:

1. For here
2. To go

Enter your choice:
""")

    if order_type == "1":
        order_type = "For here"

    elif order_type == "2":
        order_type = "To go"

    else:
        print("Invalid order type. Defaulting to For here.")
        order_type = "For here"

    # Calculate price
    coffee_price = menu[order]

    total = (coffee_price + milk_price + size_price) * quantity

    # Save order in cart
    cart.append({
        "coffee": order,
        "milk": milk_name,
        "size": size_name,
        "quantity": quantity,
        "order_type": order_type,
        "total": total
    })

    print("\nAdded to your order!")
    print("Current item total: ₹", total)

    # Ask for another coffee
    another = input(
        "\nWould you like to order another coffee? (yes/no): "
    ).lower()

    if another != "yes":
        break


# Final order summary
print("\n~ ~ ~ YOUR ORDER ~ ~ ~")

grand_total = 0

for item in cart:

    print("\nCoffee:", item["coffee"])
    print("Milk:", item["milk"])
    print("Size:", item["size"])
    print("Quantity:", item["quantity"])
    print("Order Type:", item["order_type"])
    print("Item Total: ₹", item["total"])

    grand_total += item["total"]

print("\n~ ~ ~ ~ ~ ~ ~ ~ ~ ~")
print("GRAND TOTAL: ₹", grand_total)

print("\nThank you for visiting! Enjoy your coffee!")
