
import random


class ATM:

    _bank = 'First Bank ATM'

    def __init__(self, number):  # initializer, constructors.
        self.number = number
        self.account_balance = random.randint(1000, 2000)

    def withdraw(self, amount):
        print(f"{amount} withdrawn from account number {self.number}")

    def transfer(self, amount):
        print(f"{amount} transferred from account number {self.number}")

    def check_balance(self):
        print(f"Bank Name: {self._bank} :::::: Account Balance: {self.account_balance}")

    def __repr__(self):
        return f"This object belongs to the person with :: {self.number}"


bazzan = ATM(3114233162)


kunle = ATM(3112012604)

# class Die:
#     # """Simulate a 6-sided die."""
#
#     def roll(self):
#         self.value = random.randint(1, 6)
#         return self.value
#
#     def getValue(self):
#         return self.value
#
# print(help(Die))
