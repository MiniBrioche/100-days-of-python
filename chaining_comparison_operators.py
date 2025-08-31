# age should be between 18 and 65

# normal expression:
# if age >= 18 and age < 65:

# Chaining comparison operators instead:
if 18 <= int(input("Age: ")) < 65:
    print("Eligible")
else:
    print("Denied due to Age")
