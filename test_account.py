from account import Account



def test_deposit():

    acc = Account(
        "Test",
        "ADB-001",
        1000
    )

    acc.deposit(500)

    assert acc.balance == 1500



def test_withdraw():

    acc = Account(
        "Test",
        "ADB-001",
        1000
    )

    acc.withdraw(300)

    assert acc.balance == 700



def test_negative_deposit():

    acc = Account(
        "Test",
        "ADB-001"
    )

    try:

        acc.deposit(-100)

        assert False

    except ValueError:

        assert True