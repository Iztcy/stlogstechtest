from decimal import Decimal
from Interface.BankAccountInterface import BankAccountInterface


def withdraw(account: BankAccountInterface, amount: Decimal) -> bool:
    try:
        if amount <= 0:
            raise ValueError(f"Amount cannot be 0 or negative: {amount}")

        success = account.withdraw(amount)

        if success:
            print(f'Withdraw of {amount} from {account.get_name()} successful.')
        else:
            print(f'Withdraw of {amount} from {account.get_name()} failed. Insufficient Funds.')

        return success

    except Exception as e:
        print(f"Error during withdrawal from {account.get_name()}: {e}")
        return False
