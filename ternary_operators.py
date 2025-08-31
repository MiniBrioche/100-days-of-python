# Age verification

# if age >= 18:
#    print("Eligible")
# else:
#    print("Not eligible")
# print("Age controlled")

# To avoid printing all the time, message can be used:
# if age >= 18:
#    message = "eligible for position."
# else:
#    message = "not eligible for position."
# print(message)

# To simplify even further:
message = "Eligible" if int(input("Age: ")) >= 18 else "Not eligible"
print(message)
