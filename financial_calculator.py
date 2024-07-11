import math
#finance calculator

def calculate_investment(amount, rate, years, interest_type):
    """
    Function to calculate the investment based on the provided parameters.
    """
    rate = rate / 100
    if interest_type.lower() == "simple":
        return amount * (1 + rate * years)
    elif interest_type.lower() == "compound":
        return amount * math.pow((1 + rate), years)
    else:
        raise ValueError("Invalid interest type. Please enter either 'simple' or 'compound'.")

def investment_calculator():
    # Get user input for investment details
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = int(input("Enter the number of years you plan on investing for: "))
    interest = input("Do you want 'simple' or 'compound' interest? ").lower()

    try:
        A = calculate_investment(P, r * 100, t, interest)
        print(f"The total amount after {t} years is: {A}")
    except ValueError as e:
        print(e)

def bond_calculator():
    # Get user input for bond details
    P = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    i = annual_interest_rate / 12
    n = int(input("Enter the number of months you plan to take to repay the bond: "))

    # Calculate the monthly repayment amount
    repayment = (i * P) / (1 - math.pow((1 + i), -n))

    # Print the result
    print(f"The monthly repayment amount is: {repayment}")

def main():
    """
    Main function to interact with the user and perform calculations.
    """
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond - to calculate the amount you'll have to pay on a home loan")

    choice = input("Please enter your choice: ").lower()

    if choice == 'investment':
        investment_calculator()
    elif choice == 'bond':
        bond_calculator()
    else:
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
