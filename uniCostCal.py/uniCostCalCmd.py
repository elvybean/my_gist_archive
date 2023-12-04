loop = 1
while type(loop) == int:
    maintenanceLoan = input("\n\n\nInput Maintenance Loan:  ")
    weeklyAccommodationCosts = input("Input Weekly Accommodation Costs:  ")

    x = (float(maintenanceLoan) / 3) / 12
    weeklyLoan = round(x ,2)
    y = weeklyLoan - float(weeklyAccommodationCosts)
    spendingAfterRent = round(y ,2)

    print("Your Maintenance Loan is £",maintenanceLoan," Which per week is £",weeklyLoan)
    print("If your accommodation costs £",weeklyAccommodationCosts)
    print(" This means you have £",spendingAfterRent,"left over for other spending per week.")