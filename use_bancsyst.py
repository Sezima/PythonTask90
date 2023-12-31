'User class for Banking System'

class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    def withdraw(self, draw):
        if self.balance - draw < 0:
            raise ValueError()
        else:
            self.balance -= draw
        return self.name + " has " + str(self.balance) + "."
    def check(self, name, sum):
        if not name.checking_account or name.balance < sum:
            raise ValueError()
        self.balance += sum
        name.balance -= sum
        return self.name + " has " + str(self.balance) + " and " + name.name + " has " + str(name.balance) + "."
    def add_cash(self, sum):
        self.balance += sum
        return self.name + " has " + str(self.balance) + "."


    def most_money(students):
        return self.fives * 5 + self.tens * 10 + self.twenties
