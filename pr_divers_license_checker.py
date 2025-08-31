# Checking if client is eligible for driving license
# Age >= 18 ok, Age >= 70 medical confirmation needed
# Additional challenge: wenn client 18 > age >=16 eligible for scooter license

age = int(input("Age: "))
if 70 > age >= 18:
    print("Eligible for full license.")
elif age >= 70:
    print("Medical confirmation needed.")

elif 16 <= age < 18:
    print("Scooter license available.")
else:
    print("Not eligible")

print("End of Code")
