import threading
from decimal import Decimal
from Interface.BankAccountInterface import BankAccountInterface
import time


class BankAccount(BankAccountInterface):
    def __init__(self, name: str, balance: Decimal = Decimal("0.00")):
        self.name = name
        self._balance = balance
        self._lock = threading.Lock()

    def withdraw(self, amount: Decimal) -> bool:
        with self._lock:
            if self._balance >= amount:
                time.sleep(1)
                self._balance -= amount
                return True

            return False

    def deposit(self, amount: Decimal) -> None:
        with self._lock:
            time.sleep(1)
            self._balance += amount

    def get_balance(self) -> Decimal:
        with self._lock:
            return self._balance

    def get_name(self) -> str:
        return self.name
