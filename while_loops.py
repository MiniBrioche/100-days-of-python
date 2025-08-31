number = 100
while number > 0:
    print(number)  # repeats this task as long as number is > 0
    number //= 2

command = ""
while command != "quit":  # != does not equal
    command = input(">")
    print("ECHO", command)

# To check for spelling of termination word "quit":
command = ""
while command.lower() != "quit":  # transferes input into lowercase for checking
    command = input(">")
    print("ECHO", command)
