class Account:
    
    def __init__(self, owner, number, balance=0):

        self.owner = owner
        self.account_number = number

        if balance < 0:
            raise ValueError(
                "Initial balance cannot be negative"
            )

        self.__balance = balance


    @property
    def balance(self):

        return self.__balance



    def deposit(self, amount):

        if amount <= 0:
            raise ValueError(
                "Deposit amount must be positive"
            )

        self.__balance += amount



    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError(
                "Withdrawal amount must be positive"
            )


        if amount > self.__balance:
            raise ValueError(
                "Insufficient balance"
            )


        self.__balance -= amount



    def statement(self):

        print("====================")
        print("      Addis Bank")
        print("====================")
        print(
            f"Owner: {self.owner}"
        )

        print(
            f"Account Number: {self.account_number}"
        )

        print(
            f"Balance: {self.__balance} ETB"
        )

        print("====================")