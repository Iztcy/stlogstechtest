from abc import ABC, abstractmethod
from decimal import Decimal


class BankAccountInterface(ABC):
    @abstractmethod
    def withdraw(self, amount: Decimal) -> bool:
        pass

    @abstractmethod
    def deposit(self, amount: Decimal) -> None:
        pass

    @abstractmethod
    def get_balance(self) -> Decimal:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass
