high_income = False
good_credit = True
student = True

if high_income or good_credit and not student:
    print("Eligible")

# Boolean operators are short circuit: as soon as one condition of operator
# is not met it stops checking.
