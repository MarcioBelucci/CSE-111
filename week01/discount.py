from datetime import datetime
discount_rate = 0.10
discount = 0
discount_days = [2,3]#It should work only on Wednesday and Thursdays
tax_rate = 0.06
today = datetime.now()
dow = today.weekday()
subtotal = 0
quantity = 1
while quantity != 0:
    quantity = int(input("Enter the quantity: "))
    if quantity != 0:
        price = float(input("Enter the price: $"))
        subtotal += quantity * price


print(f"Total order ${subtotal:.2f}")
if dow in discount_days:
    if subtotal >= 50:
        discount = round(subtotal * discount_rate,2)
        print(f"Discount ${discount:.2f}")
    else:
        short = 50 - subtotal
        print(f"You can get a discount by ordering {short:.2f} more")
subtotal -= discount
tax = round(subtotal * tax_rate,2)
total = subtotal + tax
print(f"Tax ${tax:.2f}")
print(f"Total Due ${total:.2f}")
