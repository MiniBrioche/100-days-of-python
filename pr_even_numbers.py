count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1  # counting iterations
        print(number)
print(f"We have {count} even numbers.")  # formatted string needed!
