print("Shipping Calculator")
print()
total = 0
price = 0
number = int(input("Number of Items:"))
if number < 0:
    print('Invalid entry')
    number = int(input("Number of Items:"))
for i in range(0,number,1):
    price = float(input("Price of item:"))
    total = total + price
if total > 100:
    total = total * 90 / 100
print("Total price for", number,"items is ${:.2f}".format(total))