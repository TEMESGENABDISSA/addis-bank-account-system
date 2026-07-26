from account import Account


class CurrentAccount(Account):

    def __init__(self, owner, number, balance=0, overdraft=1000):
        super().__init__(owner, number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance + self.overdraft:
            raise ValueError("Over limit")

        self._Account__balance -= amount

    def statement(self):
        return (
            f"Account Type: Current\n"
            f"Owner: {self.owner}\n"
            f"Account: {self.account_number}\n"
            f"Balance: {self.balance} ETB"
        )