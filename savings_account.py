from account import Account


class SavingsAccount(Account):

    def __init__(self, owner, number, balance=0, interest_rate=0.05):

        super().__init__(
            owner,
            number,
            balance
        )

        self.interest_rate = interest_rate


    def calculate_interest(self):

        return self.balance * self.interest_rate