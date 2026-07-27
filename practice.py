# ==========================================
# ADDIS BANK - PRACTICE / DEMONSTRATION
# ==========================================


# ==========================================
# DAY 4 - ACCOUNT
# ==========================================

from account import Account

account = Account(
    "Almaz",
    "ADB-001",
    5000
)

account.deposit(1000)
account.withdraw(500)

account.statement()


# ==========================================
# DAY 5 - INHERITANCE
# ==========================================

from savings_account import SavingsAccount
from current_account import CurrentAccount

savings = SavingsAccount(
    "Almaz",
    "ADB-002",
    5000
)

current = CurrentAccount(
    "Dawit",
    "ADB-003",
    1000
)

savings.add_interest()

savings.statement()
current.statement()


# ==========================================
# POLYMORPHISM
# ==========================================

accounts = [
    account,
    savings,
    current
]

for acc in accounts:
    acc.statement()


# ==========================================
# DAY 6 - FACTORY
# ==========================================

from account_factory import AccountFactory

new_account = AccountFactory.create(
    "savings",
    "Hana",
    "ADB-004",
    3000
)

new_account.statement()


# ==========================================
# DAY 7 - REGISTRY
# ==========================================

from account_registry import AccountRegistry

registry = AccountRegistry()

registry.add(account)
registry.add(savings)
registry.add(current)

print(registry.find("ADB-001"))

print(registry.list_all())


# ==========================================
# DAY 8 - ALGORITHMS
# ==========================================

# Put your actual algorithm demonstrations here.


# ==========================================
# DAY 9 - TREE
# ==========================================

from branch import Branch

head_office = Branch("Head Office")
bole = Branch("Bole")

head_office.add_child(bole)
bole.add_account(account)

print(head_office.total_balance())


# ==========================================
# DAY 9 - GRAPH
# ==========================================

from transfer_graph import TransferGraph

graph = TransferGraph()

graph.add_transfer("ADB-001", "ADB-002")
graph.add_transfer("ADB-002", "ADB-003")

print(graph.bfs("ADB-001"))


# ==========================================
# DAY 9 - PRIORITY QUEUE
# ==========================================

from payment_queue import PaymentQueue

payments = PaymentQueue()

payments.add_payment(4, "Airtime")
payments.add_payment(1, "Rent")
payments.add_payment(2, "School fees")

while payments.queue:
    print(payments.process_payment())