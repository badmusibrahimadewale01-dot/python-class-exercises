   # TODO: check that it is all digits and has length 10
    # If valid -> break loop, else keep asking

while True:
    account_number = input("Enter your 10-digit account number: ")

    if account_number.isdigit() and len(account_number) == 10:
        print("Valid account number.")
        break
    else:
        print("Invalid account number. Please try again.")  
        
