import pytest

from account import Account


def test_account_creation():
    account = Account("Almaz", "ADB-001", 5000)

    assert account.owner == "Almaz"
    assert account.account_number == "ADB-001"
    assert account.balance == 5000


def test_deposit():
    account = Account("Almaz", "ADB-001", 5000)

    account.deposit(1000)

    assert account.balance == 6000


def test_withdraw():
    account = Account("Almaz", "ADB-001", 5000)

    account.withdraw(1000)

    assert account.balance == 4000


def test_negative_deposit():
    account = Account("Almaz", "ADB-001", 5000)

    with pytest.raises(ValueError):
        account.deposit(-100)


def test_zero_deposit():
    account = Account("Almaz", "ADB-001", 5000)

    with pytest.raises(ValueError):
        account.deposit(0)


def test_overdraft_is_rejected():
    account = Account("Almaz", "ADB-001", 500)

    with pytest.raises(ValueError):
        account.withdraw(1000)