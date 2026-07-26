from account import Account
from algorithms import (
    rank_accounts,
    binary_search,
    find_pair,
    total_balance
)


accounts = [
    Account("Almaz", "ADB-1", 5000),
    Account("Dawit", "ADB-2", 2000),
    Account("Abebe", "ADB-3", 8000)
]


# A. Ranking
print("A. Ranked accounts:")

for account in rank_accounts(accounts):
    print(account.owner, account.balance)


# B. Binary search
numbers = [
    "ADB-1",
    "ADB-2",
    "ADB-3",
    "ADB-4"
]

print("\nB. Binary search:")
print(binary_search(numbers, "ADB-3"))


# C. Two pointers
balances = [1000, 2000, 3000, 4000, 5000]

print("\nC. Two pointers:")
print(find_pair(balances, 6000))


# D. Recursion
print("\nD. Total balance:")
print(total_balance(accounts))