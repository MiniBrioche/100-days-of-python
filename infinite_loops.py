while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

# From file "while_loops": a better way to write the same code
# command = ""
# while command.lower() != "quit":  # transferes input into lowercase for checking
#    command = input(">")
#    print("ECHO", command)
