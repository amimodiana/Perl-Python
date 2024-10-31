
# Derived class for Savings Account

class Account:

    def __init__(self, account_number, account_holder, balance=0):

        self.account_number = account_number

        self.account_holder = account_holder

        self.balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.balance += amount

            return f"Deposited ksh{amount}. New balance: ksh{self.balance}"

        else:

            return "Deposit amount must be positive."

    def withdraw(self, amount):

        if 0 < amount <= self.balance:

            self.balance -= amount

            return f"Withdrew ksh{amount}. Remaining balance: ksh{self.balance}"

        else:

            return "Invalid withdrawal amount or insufficient funds."

    def get_balance(self):

        return f"Account balance: ksh{self.balance}"



class SavingsAccount(Account):

    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)

        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate

        self.balance += interest

        return f"Interest of ksh{interest:.2f} applied. New balance: ksh{self.balance:.2f}"  # Derived class for Checking Account


class CheckingAccount(Account):

    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):

        super().__init__(account_number, account_holder, balance)

        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if 0 < amount <= self.balance + self.overdraft_limit:

            self.balance -= amount

            return f"Withdrew ksh{amount}. Remaining balance: ksh{self.balance}"

        else:
            class BankAccount:

                def init(self, balance):

                    self._balance = balance  # Protected attribute

                def deposit(self, amount):

                    if amount > 0:

                        self._balance += amount

                    else:

                        print("Amount must be positive")

                def get_balance(self):

                    return self._balance

                return "Invalid withdrawal amount or insufficient funds."

                def get_balance(self):

                    return f"Account balance: ksh{self.balance}"

            class SavingsAccount(Account):

                def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
                    super().__init__(account_number, account_holder, balance)

                    self.interest_rate = interest_rate

                def apply_interest(self):
                    interest = self.balance * self.interest_rate

                    self.balance += interest

                    return f"Interest of ksh{interest:.2f} applied. New balance: ksh{self.balance:.2f}"  # Derived class for Checking Account

            class CheckingAccount(Account):

                def __init__(self, account_number, account_holder, balance=0, overdraft_limit=100):
                    super().__init__(account_number, account_holder, balance)

                    self.overdraft_limit = overdraft_limit

                def withdraw(self, amount):
                    if 0 < amount <= self.balance + self.overdraft_limit: