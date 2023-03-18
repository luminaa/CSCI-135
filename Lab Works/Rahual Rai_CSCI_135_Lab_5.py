class BankAccount:

    # initialize the BankAccount instance
    def __init__(self, pin):
        self.pin = pin
        self.balance = 0

    # deposit money into the account
    def deposit(self, pin, amount):
        if self.pin != pin: # if pin is invalid, return wrong pin message
            print("Invalid PIN")
            return
        self.balance += amount # if pin is correct, add the amount to the balance and return a success message
        print(f"Deposited ${amount} successfully. Available balance: ${self.balance}")

    # withdraw money from the account
    def withdraw(self, pin, amount):
        if self.pin != pin: # if pin is invalid, return wrong pin message
            print("Invalid PIN")
            return
        if amount > self.balance: # if withdrawal amount is greater than the balance, return error message
            print("Withdrawal canceled. Available balance is lower than the requested amount.")
            return
        self.balance -= amount # withdrawal is successful, subtract the amount from the balance and return a success message
        print(f"Withdrawn ${amount} successfully. Available balance: ${self.balance}")

    # get the current balance of the account
    def get_balance(self, pin):
        if self.pin != pin: # if pin is invalid, return wrong pin message
            print("Invalid PIN")
            return
        print(f"Available balance: ${self.balance}") # print the current balance

# create an instance of BankAccount with PIN 1234
my_account = BankAccount(1234)

# deposit $100 to my account
my_account.deposit(1234, 100)

# withdraw $50 from my account
my_account.withdraw(1234, 50)

# get the current balance of my account
my_account.get_balance(1234)

"""
Output: 
Deposited $100 successfully. Available balance: $100
Withdrawn $50 successfully. Available balance: $50
Available balance: $50
"""