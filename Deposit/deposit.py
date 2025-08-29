from decimal import Decimal
from Interface.BankAccountInterface import BankAccountInterface


def deposit(account: BankAccountInterface, amount: Decimal) -> bool:
    try:
        if amount <= 0:
            raise ValueError(f"Amount cannot be 0 or negative: {amount}")

        account.deposit(amount)

        print(f'Deposit of {amount} to {account.get_name()} successful.')

        return True

    except Exception as e:
        print(f"Error during deposit to {account.get_name()}: {e}")
        return False
