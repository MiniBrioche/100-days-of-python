# Ask for principal, rate, and time (years) → print the total amount after interest.
# A = P × (1 + rt))

p = int(input("Principal: "))
r = float(input("Rate in %: ")) / 100  # Converting to decimal
t = int(input("Time in years: "))

print(f"The total amount is {int(p) * (1 + r * t)} Euros.")
