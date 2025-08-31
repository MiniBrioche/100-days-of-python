x = int(input("Please enter a number between 1 and 100: "))

if 0 < x < 101:
    trollcheck = True
    print("Number accepted.")
    for number in range(1, x+1):  # 1 in beginning to avoid 0 being labeled.
        if number % 2 == 0:
            print(number, "even.")
        else:
            print(number, "odd.")
else:
    trollcheck = False
    print("Haha nice try.")
