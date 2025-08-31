# 1 cat year = 15 human years
# 2 cat years = 24 human years
# Each year after = +4 human years

c = int(input("Please enter your cat's age in cat years: "))

if c == 1:
    print("Your cat is 15 human years old.")
elif c == 2:
    print("Your cat is 24 human years old.")
elif c > 2:
    h = 24 + (c - 2) * 4  # subtracting 2 to avoid overcalculation
    print(f"Your cat is {h} human years old.")
else:
    print("That doesn't seem like a valid cat age.")
