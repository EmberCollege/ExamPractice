while True:

    for n in range(0,5):
        number = input("Enter the amount you spent on the last 5 transactions you made: ")

    try:
        float(number)
        VAT = number / 5
        round(VAT,2)
        numberIncVAT = number + VAT
        print("Your cost without VAT is", number, "and including VAT is", numberIncVAT)
        break
    except:
        number = input("Please enter a number")
        break