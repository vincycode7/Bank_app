class Bankingapp:
    total_user = 0

    def __init__(self, name=None, email=None, passwrd=None):
        self.balance = 0
        self.name = name
        self.email = email
        self.passwrd = passwrd
        self.unique_id = self.incr_total_user()


    def check_balance(self):
        return self.balance

    def deposit(self, amount=None):
        self.balance += amount
        return 1

    def withdraw(self, amount = None):
        if (self.balance - amount) >= 0:
            self.balance -= amount

            return 1
        else:
            return 0
        

    def transfer(self, amount=None, to_id=None):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            to_id.balance += amount
            return (to_id, 1)
        else:
            return (to_id,0)
        
    @classmethod
    def incr_total_user(cls):
        current_user_id = cls.total_user
        cls.total_user += 1
        return current_user_id