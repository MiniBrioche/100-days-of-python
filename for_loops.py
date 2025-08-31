for number in range(3):
    print("Attempt")  # prints "attempt 3 times looped"

for number in range(3):
    print("Attempt", number + 1)  # prints the above but also counts up from 0

for number in range(3):
    # A string multiplied by a number repeats the string counting up
    print("Attempt", number + 1, (number + 1) * '.')

for number in range(1, 4):  # 1 is beginning, 4 the end. +1 therefore not needed anymore
    print("Attempt", number, number * '.')

for number in range(1, 4, 2):  # 2 is called a "step" that will be left out of the count
    print("Attempt", number, number * '.')
