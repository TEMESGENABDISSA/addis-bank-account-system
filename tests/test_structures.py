from account import Account
from branch import Branch
from transfer_graph import TransferGraph
from payment_queue import PaymentQueue


def test_branch_total_balance():
    head = Branch("Head Office")
    bole = Branch("Bole")

    head.add_child(bole)

    account = Account(
        "Almaz",
        "ADB-001",
        5000
    )

    bole.add_account(account)

    assert head.total_balance() == 5000


def test_transfer_graph():
    graph = TransferGraph()

    graph.add_transfer("ADB-001", "ADB-002")
    graph.add_transfer("ADB-002", "ADB-003")

    reachable = graph.bfs("ADB-001")

    assert "ADB-001" in reachable
    assert "ADB-002" in reachable
    assert "ADB-003" in reachable


def test_payment_queue():
    queue = PaymentQueue()

    queue.add_payment(4, "Airtime")
    queue.add_payment(1, "Rent")
    queue.add_payment(2, "School fees")

    priority, payment = queue.process_payment()

    assert priority == 1
    assert payment == "Rent"