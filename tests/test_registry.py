from account import Account
from account_registry import AccountRegistry


def test_add_and_find_account():
    registry = AccountRegistry()

    account = Account(
        "Almaz",
        "ADB-001",
        5000
    )

    registry.add(account)

    found = registry.find("ADB-001")

    assert found is account


def test_list_all():
    registry = AccountRegistry()

    account1 = Account("Almaz", "ADB-001", 5000)
    account2 = Account("Dawit", "ADB-002", 3000)

    registry.add(account1)
    registry.add(account2)

    accounts = registry.list_all()

    assert accounts == [account1, account2]