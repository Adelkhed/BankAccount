class BankAccount:
    all_accounts = []

    def __init__(self, interest_rate=0, balance=0):
        self.balance = balance
        self.interest_rate = interest_rate
        self.__class__.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%")
        return self

    def yield_interest(self):
        self.balance += self.balance * self.interest_rate
        return self

    @classmethod
    def display_all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()
    
account1 = BankAccount(0.02, 1000)
account2 = BankAccount(0.05, 500)


account1.deposit(100).deposit(200).deposit(300).withdraw(150).yield_interest().display_account_info()

account2.deposit(50).deposit(75).withdraw(30).withdraw(20).withdraw(10).withdraw(5).yield_interest().display_account_info()

BankAccount.display_all_accounts_info()
