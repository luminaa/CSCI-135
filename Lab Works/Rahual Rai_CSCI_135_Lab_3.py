class BankAccount:
 
    def __init__(self, pin): # initializes intance object
        self.pin = pin # sets the pin for the account instance, compared agains this for every transaction
        self.balance = 0 # balance for the account instance is set to zero
    
    def deposit(self, pin, amount): 
        if self.pin == pin: # correct pin must be given
            self.balance += amount # adds money deposited to the account balance
            print("Deposit successful.")
        else: # if incorrect pin is given, transaction is canceled
            print("Incorrect pin. Transaction canceled.")
        print()
    
    def withdraw(self, pin, amount):
        if self.pin == pin: # correct pin must be given
            if amount > self.balance: # check if amount is greater than the balance available in the account
                print("The available balance is lower than the requested amount. Transaction canceled.")
            else:  # account has sufficient money to withdraw the amount
                self.balance -= amount # subtract the amount from the account balance
                print("Withdrawal successful.")
        else: # if incorrect pin is given, transaction is canceled
            print("Incorrect pin. Transaction canceled.")
        print()
    
    def get_balance(self, pin):
        if self.pin == pin: # correct pin must be given
            print("Your current balance is " + str(self.balance))
        else: # if incorrect pin is given, transaction is canceled
            print("Incorrect pin. Transaction canceled.")
        print()









example_account = BankAccount(123456)
example_account.get_balance(123456)
example_account.get_balance(12346)
example_account.withdraw(123456,3)
example_account.deposit(123456, 1000000000)
example_account.get_balance(123456)
example_account.withdraw(123456, 12312312)
example_account.get_balance(123456)