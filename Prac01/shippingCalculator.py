totalShipping = 0
itemNum = int(input("Enter the number of items: "))
while itemNum < 0:
    print("Invalid number of items!")
    itemNum = int(input("Enter the number of items:"))
for i in range(itemNum):
    totalShipping = totalShipping + float(input("Enter the price of item:"))

if totalShipping > 100:
    totalShipping = totalShipping * 0.9

print("Total Price for", itemNum, "items is", totalShipping)
