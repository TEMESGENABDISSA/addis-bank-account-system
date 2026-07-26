class AccountRegistry:
    
    def __init__(self):
        self.by_number = {}
        self.order = []
        self.history = {}

    def add(self, account):
        self.by_number[account.account_number] = account
        self.order.append(account.account_number)
        self.history[account.account_number] = []

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):
        return [
            self.by_number[number]
            for number in self.order
        ]