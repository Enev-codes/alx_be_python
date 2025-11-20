import uuid, pickle, numbers

class BankAccount:
    '''Blueprint for bank account'''
    def __init__(self, account_balance=0):
        '''Initializes the account'''
        self._id = uuid.uuid4()
        self.account_balance = 0

    def deposit(self, amount):
        '''Adds <amount> to the existing account balance'''
        if isinstance(amount, numbers.Number):
            self.account_balance += amount

    def withdraw(self, amount):
        '''Deducts <amount> from existing account balance (if sufficient)'''
        if isinstance(amount, numbers.Number):
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            return False
        return False

    def display_balance(self):
        '''Displays <self.account_balance> of account'''
        print(f"Current Balance: $[{self.account_balance}]")

    def serialize(self, *args, **kwargs):
        '''Write Python object into string or file'''
        with open('accounts.db', 'wb') as file:
            pickle.dump(self, file)

    def deserialize(self, *args, **kwargs):
        '''Reads serialized data into code as actual python objects'''
        with open('account.db', 'rb') as file:
            aza = pickle.load(file)
