from decimal import Decimal
from Interface.BankAccountInterface import BankAccountInterface
import time


class BankAccountNonConcurrency(BankAccountInterface):
    def __init__(self, name: str, balance: Decimal = Decimal("0.00")):
        self.name = name
        self._balance = balance

    def withdraw(self, amount: Decimal) -> bool:
        if self._balance >= amount:
            time.sleep(1)
            self._balance -= amount
            return True

        return False

    def deposit(self, amount: Decimal) -> None:
        time.sleep(1)
        self._balance += amount

    def get_balance(self) -> Decimal:
        return self._balance

    def get_name(self) -> str:
        return self.name
