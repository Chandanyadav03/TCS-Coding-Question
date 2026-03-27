# Step 1: Take input from user
amount = int(input("Enter purchase amount: "))

# Step 2: Apply discount based on conditions
if amount < 1000:
    discount = 0.05   # 5%
elif amount >= 1000 and amount < 5000:
    discount = 0.10   # 10%
else:
    discount = 0.15   # 15%

# Step 3: Calculate final amount
final_amount = amount - (amount * discount)

# Step 4: Print result rounded to 2 decimal places
print("Final payable amount: {:.2f}".format(final_amount))