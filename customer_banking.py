# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    print("Hello! Let's create a new account!")
    savings_balance = float(input("What is the current balance of the account? "))
    savings_interest = float(input("What is the interest rate of the account? ie 5 for 5% "))
    savings_maturity = int(input("How many months will you be holding the account? "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The new balance of the account after maturity is ${updated_savings_balance: ,.2f} and your interest earned amounts to ${interest_earned: ,.2f}.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    print("Next, we'll create a certificate of deposit(CD) account! Please note that some CD accounts may have a minimum maturity period, and your payout may be penalized if you withdraw too early.")
    cd_balance = float(input("What is the current balance of the account? "))
    cd_interest = float(input("What is the interest rate of the account? ie 5 for 5% "))
    cd_maturity = int(input("How many months will you be holding the account? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The new balance of the account after maturity is ${updated_cd_balance: ,.2f} and your interest earned amounts to ${interest_earned: ,.2f}.")
    print("Thank you for opening an account with us today!")

if __name__ == "__main__":
    # Call the main function.
    main()