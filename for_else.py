successful = True

for number in range(3):
    print("Attempt")
    if successful:  # We are checking the boolean with every attempt
        print("Successful")
        break  # and if that is the case, we jump out of the loop.
else:  # kicks in once count (in this case 3) is over and "if" hasn't triggered
    print("Attempted 3 times and failed")
