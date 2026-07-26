from savings_account import SavingsAccount
from current_account import CurrentAccount


class AccountFactory:

    @staticmethod
    def create(kind, owner, number, balance=0):

        if kind == "savings":
            return SavingsAccount(owner, number, balance)

        if kind == "current":
            return CurrentAccount(owner, number, balance)

        raise ValueError("Unknown account type")