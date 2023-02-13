menu = ["tuna sandwich", "pain au chocolat", "cheese toastie", "snack bar"]
stock = {"tuna sandwich": 5, "pain au chocolat": 4, "cheese toastie": 7, "snack bar": 13}
price = {"tuna sandwich": "£4.99", "pain au chocolat": "£2.50", "cheese toastie": "£3.99", "snack bar": "£1.99"}

total_price = 0

for food in menu:
    total += stock[food] * price[food]

print(total)