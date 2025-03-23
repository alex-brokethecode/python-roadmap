# Create a BankAccount class with a private attribute _balance. Add methods to deposit, withdraw, and get balance

class BankAccount:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float) -> None:
        if balance < 0:
            raise ValueError('Balance cannot be negative')

        self.__balance = balance

    def deposit(self, amount: float) -> None:
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self.__balance:
            raise ValueError('Insufficient funds')

        self.__balance -= amount


if __name__ == '__main__':
    try:
        account = BankAccount(-1000)
        account.deposit(500)
        account.withdraw(200)
        print(account.balance)
    except ValueError as e:
        print(e)
