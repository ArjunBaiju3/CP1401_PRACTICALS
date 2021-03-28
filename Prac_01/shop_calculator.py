total = 0
no_of_items = int(input("Number of items: "))

while no_of_items < 0:
    print("Invalid number of items!")
    no_of_items = int(input("Number of items: "))

for i in range(no_of_items):
    print(i + 1, end=' ')
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for {} items is ${:.2f}".format(no_of_items, total))
