import math

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

def main():
    """
    Main function to interact with the user and perform calculations.
    """
    print("Choose either 'investment' or 'bond' from the menu below to proceed:")
    print("investment - to calculate the amount of interest you'll earn on interest")
    print("bond - to calculate the amount you'll have to pay on a home loan")

    choice = input("Please enter your choice: ").lower()

    if choice == 'investment':
        amount = float(input("Enter the amount of money that you are depositing: "))
        rate = float(input("Enter the interest rate (as a percentage): "))
        years = float(input("Enter the number of years you plan on investing for: "))
        interest_type = input("Do you want 'simple' or 'compound' interest: ")

        try:
            final_amount = calculate_investment(amount, rate, years, interest_type)
            print(f"After {years} years at an interest rate of {rate}%, you will have: {final_amount}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

if __name__ == "__main__":
    main()
