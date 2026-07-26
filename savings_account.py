from account import Account


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0, rate=0.05):
        super().__init__(owner, number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        return (
            f"Account Type: Savings\n"
            f"Owner: {self.owner}\n"
            f"Account: {self.account_number}\n"
            f"Balance: {self.balance} ETB"
        )