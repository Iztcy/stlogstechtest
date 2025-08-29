import threading
from decimal import Decimal
from Account.BankAccount import BankAccount
from Account.BankAccountNonConcurrency import BankAccountNonConcurrency
from Withdraw.withdraw import withdraw
from Deposit.deposit import deposit


def run():
    # alice_account = BankAccountNonConcurrency("Alice")
    # bob_account = BankAccountNonConcurrency("Bob")

    alice_account = BankAccount("Alice")
    bob_account = BankAccount("Bob")

    print("Alice initial balance: ", alice_account.get_balance())
    print("Bob initial balance: ", bob_account.get_balance())

    deposit(alice_account, Decimal("5000"))
    deposit(bob_account, Decimal("3400"))

    print("Alice balance: ", alice_account.get_balance())
    print("Bob balance: ", bob_account.get_balance())

    threads = [
        threading.Thread(target=withdraw, args=(alice_account, Decimal("3500"))),
        threading.Thread(target=withdraw, args=(alice_account, Decimal("3500"))),
        threading.Thread(target=withdraw, args=(bob_account, Decimal("2500"))),
        threading.Thread(target=withdraw, args=(bob_account, Decimal("1800"))),
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("Final Output:")
    print("Alice balance: ", alice_account.get_balance())
    print("Bob balance: ", bob_account.get_balance())


if __name__ == "__main__":
    run()
