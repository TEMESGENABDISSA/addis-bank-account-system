from account import Account
from algorithms import (
    rank_accounts,
    binary_search,
    find_pair,
    total_balance
)


def test_rank_accounts():
    account1 = Account("Almaz", "ADB-001", 5000)
    account2 = Account("Dawit", "ADB-002", 2000)
    account3 = Account("Hana", "ADB-003", 8000)

    accounts = [account1, account2, account3]

    result = rank_accounts(accounts)

    assert result[0].balance == 8000
    assert result[1].balance == 5000
    assert result[2].balance == 2000


def test_binary_search():
    numbers = [10, 20, 30, 40, 50]

    assert binary_search(numbers, 30) == 2
    assert binary_search(numbers, 50) == 4
    assert binary_search(numbers, 100) == -1


def test_find_pair():
    balances = [1000, 2000, 3000, 4000]

    result = find_pair(balances, 5000)

    assert result == (1000, 4000)


def test_find_pair_not_found():
    balances = [1000, 2000, 4000]

    result = find_pair(balances, 10000)

    assert result is None


def test_total_balance():
    account1 = Account("Almaz", "ADB-001", 5000)
    account2 = Account("Dawit", "ADB-002", 3000)
    account3 = Account("Hana", "ADB-003", 2000)

    accounts = [account1, account2, account3]

    assert total_balance(accounts) == 10000


def test_total_balance_empty():
    assert total_balance([]) == 0