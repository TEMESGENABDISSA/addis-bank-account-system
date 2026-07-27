import pytest

from savings_account import SavingsAccount
from current_account import CurrentAccount


def test_savings_account():
    account = SavingsAccount(
        "Almaz",
        "ADB-001",
        5000,
        0.05
    )

    account.add_interest()

    assert account.balance == 5250


def test_current_account_allows_overdraft():
    account = CurrentAccount(
        "Dawit",
        "ADB-002",
        1000,
        500
    )

    account.withdraw(1200)

    assert account.balance == -200


def test_current_account_rejects_large_overdraft():
    account = CurrentAccount(
        "Dawit",
        "ADB-002",
        1000,
        500
    )

    with pytest.raises(ValueError):
        account.withdraw(1600)