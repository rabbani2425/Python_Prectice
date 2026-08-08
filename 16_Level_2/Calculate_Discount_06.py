# Calculate the discount based on the amount.

amount = float(input("Enter the purchase amount: "))

if amount >= 5000:
    discount = amount * 20 / 100
elif amount >= 2000:
    discount = amount * 10 / 100
else:
    discount = 0

final_amount = amount - discount

print("Discount: Rs.", discount )
print("Final Amount: Rs.", final_amount)