class Branch:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.accounts = []

    def add_child(self, branch):
        self.children.append(branch)

    def add_account(self, account):
        self.accounts.append(account)

    def total_balance(self):
        total = sum(
            account.balance
            for account in self.accounts
        )

        for child in self.children:
            total += child.total_balance()

        return total