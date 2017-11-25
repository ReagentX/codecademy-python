class BankAccount(object):
    """Base class for a bank account"""
    balance = 0.
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Account belongs to {self.name} and has ${self.balance:.2f}'

    def show_balance(self):
        """Prints the balance of an account"""
        print(f'${self.balance:.2f}')

    def deposit(self, amount):
        """Deposits an amount into an account's balance if that amount is positive"""
        if amount > 0:
            print(f'Depositing ${amount:.2f}')
            self.balance += amount

    def withdraw(self, amount):
        """Withdraws an amount from an account's balance if that amount is positive and the account will not overdraft"""
        if amount > 0 and self.balance - amount > 0:
            print(f'Withdrawing ${amount:.2f}')
            self.balance -= amount
        else:
            print(f'Insufficient funds to withdraw ${amount:.2f}')


my_account = BankAccount('Chris')
print(my_account)
my_account.deposit(2000)
my_account.show_balance()
my_account.withdraw(1000)
my_account.show_balance()
