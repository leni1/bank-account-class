class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = bool()

    def get_balance(self):
        if self.is_open:
            return self.balance
        raise ValueError

    def open(self):
        self.is_open = True
        return self.is_open

    def deposit(self, amount):
        if amount < 0 or not self.is_open:
            raise ValueError
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance or amount < 0:
            raise ValueError
        self.balance -= amount
        return self.balance

    def close(self):
        self.is_open = False
        return self.is_open
