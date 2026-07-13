from account import Account



account1 = Account(
    "Almaz",
    "ADB-1001",
    1500
)


account2 = Account(
    "Abebe",
    "ADB-1002",
    3000
)



account1.deposit(500)

account1.withdraw(200)



account2.deposit(1000)



account1.statement()

account2.statement()



print(
    "Account 1 balance:",
    account1.balance
)


print(
    "Account 2 balance:",
    account2.balance
)