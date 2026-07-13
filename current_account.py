from account import Account


class CurrentAccount(Account):

    def __init__(
        self,
        owner,
        number,
        balance=0,
        overdraft_limit=5000
    ):

        super().__init__(
            owner,
            number,
            balance
        )

        self.overdraft_limit = overdraft_limit 