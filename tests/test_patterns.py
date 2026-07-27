from bank_config import BankConfig
from account_factory import AccountFactory


def test_singleton():
    first = BankConfig()
    second = BankConfig()

    assert first is second


def test_factory_creates_savings():
    account = AccountFactory.create(
        "savings",
        "Almaz",
        "ADB-001",
        5000
    )

    assert account.owner == "Almaz"
    assert account.account_number == "ADB-001"
    assert account.balance == 5000


def test_factory_creates_current():
    account = AccountFactory.create(
        "current",
        "Dawit",
        "ADB-002",
        3000
    )

    assert account.owner == "Dawit"
    assert account.balance == 3000