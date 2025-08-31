# Loan verification

# and > both booleans need true
# or > either boolean needs true
# not > boolean needs false

high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
