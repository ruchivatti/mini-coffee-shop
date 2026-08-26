menu = {
    "americano": 100,
    "latte": 150,
    "cappuccino": 200,
    "espresso": 120,
    "mocha": 180
}

print("~ ~ ~ COFFEE MENU ~ ~ ~")
for coffee, price in menu.items():
    print(coffee,"₹",price)

order = input("What coffee would you like to order? ")

if order in menu:
    print("You selected",order)
else:
    print("Sorry, we don't have that coffee on the menu.")

quantity = int(input("How many cups would you like to order? "))
total = menu[order] * quantity

print("You ordered",quantity,"cups of",order,"for a total of ₹",total)

print("Enjoy your drink!")