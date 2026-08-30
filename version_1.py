
menu = {
    "americano": 100,
    "latte": 150,
    "cappuccino": 200,
    "espresso": 120,
    "mocha": 180
}

print("\n~ ~ ~ ☕ COFFEE MENU ~ ~ ~")

for coffee, price in menu.items():
    print(coffee, "₹", price)

# Coffee selection
order = input("\nWhat coffee would you like to order? ").lower()

if order in menu:
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
2. Medium
3. Large

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
        print("Invalid size choice. Defaulting to 'Small'.")
        size_name = "Small"
        size_price = 0

    # Quantity
    quantity = int(input("\nHow many cups would you like? "))

    #order_type
    order_type=input("""
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
        print("Invalid order type. Defaulting to 'For here'.")
        order_type = "For here"

    # Calculate total
    coffee_price = menu[order]
    total = (coffee_price + milk_price) * quantity

    # Order summary
    print("\n~ ~ ~ YOUR ORDER ~ ~ ~")
    print("Coffee:", order)
    print("Milk:", milk_name)
    print("Size:", size_name)
    print("Quantity:", quantity)
    print("Order Type:",order_type)
    print("Total: ₹", total)

    print("\n☕ Enjoy your drink!")

else:
    print("Sorry, we don't have that coffee on the menu.")
