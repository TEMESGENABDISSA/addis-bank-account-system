def rank_accounts(accounts):
    return sorted(
        accounts,
        key=lambda account: account.balance,
        reverse=True
    )


def binary_search(numbers, target):

    left = 0
    right = len(numbers) - 1

    while left <= right:

        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        if numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


def find_pair(balances, target):

    balances.sort()

    left = 0
    right = len(balances) - 1

    while left < right:

        total = balances[left] + balances[right]

        if total == target:
            return balances[left], balances[right]

        if total < target:
            left += 1

        else:
            right -= 1

    return None


def total_balance(accounts):

    if not accounts:
        return 0

    return accounts[0].balance + total_balance(accounts[1:])