# loan amount
# Annual Percentage Rate (APR)
# loan duration - yrs
# m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

# ask user for loan duration in years
# ask user for loan duration in additional months
# ask for loan amount
# ask for APR in % amounts to nearest hundredth
# convert APR to monthly interest rate
# convert loan duration to total months
# calculate monthly payment amount
# print monthly payment amount in dollar and cents format $123.00

def monthly_bill(loan_amount, duration, interest_rate):
    interest_rate = interest_rate / 100

    if not interest_rate:
        return loan_amount / duration
    
    monthly_amount = loan_amount * (interest_rate /
                    (1 - (1 + interest_rate) ** (-duration)))
    return monthly_amount

def prompt(message):
    print(f"==> {message}")

def invalid_value(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

def invalid_duration(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt("Let's calculate the monthly payments for this loan!")

while True:
    prompt("Please input the amount of the loan:")
    loan = input("$")

    while invalid_value(loan) or float(loan) <= 0:
        prompt("Please enter a positive entry:")
        loan = input("$")

    loan = float(loan)

    prompt("Let's get the duration for this loan in years and months.")
    prompt("First input the number of years:")
    years = input()

    while invalid_duration(years) or int(years) < 0:
        prompt("Please enter a number greater than or equal to 0:")
        years = input()

    years = int(years)

    prompt("Now input the number of additional months if any:")
    months = input()

    while invalid_duration(months) or int(months) < 0:
        prompt("Please enter a number greater than or equal to 0:")
        months = input()

    months = 12 * years + int(months)

    prompt("What is your annual interest rate? "
           "e.g. 10 for 10% or 4.5 for 4.5%")
    apr = input()
    while invalid_value(apr) or float(apr) < 0:
        prompt("Please enter a number greater than or equal to 0.")
        apr = input()

    apr = float(apr)
    monthly_pct_rate = apr / 12

    monthly_payment = monthly_bill(loan, months, monthly_pct_rate)
    print(f"The monthly payment is ${monthly_payment:.2f}")

    prompt("Do you want another calculation? y/n")
    response = input().lower()

    while response not in ("n", "no", "y", "yes"):
        prompt('Please enter y for "yes" or n for "no"')
        response = input().lower()

    if response in ("n", "no"):
        break