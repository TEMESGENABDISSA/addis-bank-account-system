class Account:
    def __init__(self, owner, number, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.owner = owner
        self.account_number = number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount

    def statement(self):
        return (
            f"Owner: {self.owner}\n"
            f"Account: {self.account_number}\n"
            f"Balance: {self.balance} ETB"
        )