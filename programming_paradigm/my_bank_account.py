# Goal: Understand the fundamentals of OOP in Python by implementing a
# BankAccount class that encapsulates banking operations. Use command line
# arguments to interact with instances of this class.
# Check ./main-0.py for usage
import uuid, pickle, numbers

class BankAccount:
    '''Blueprint for bank account'''
    _account_balance = 0
    _accounts = []

    def __init__(self, _account_balance=0):
        '''Initializes an account with <_account_balance>'''
        self._id = str(uuid.uuid4())
        self._account_balance = BankAccount._account_balance
        BankAccount._accounts.append(self)

    def deposit(self, amount):
        '''Deserializes `./accounts.db` file back into the <_accounts> python array'''
        '''Updates (Add) <amount> to the existing account balance (if any)'''
        '''Serializes <_accounts> python array back into `./accounts.db` file'''
        if isinstance(amount, numbers.Number):
            accs = BankAccount.deserialize(self._id) 
            if accs:
                for acc in accs:
                    if acc._id == self._id:
                        acc._account_balance += amount
        BankAccount.serialize(BankAccount._accounts)

    def withdraw(self, amount):
        '''Deserializes `./accounts.db` file back into the python array'''
        '''Updates (Sub) <amount> from existing account balance (if sufficient)'''
        '''Serializes <_accounts> to <accounts.db> file'''
        if isinstance(amount, numbers.Number):
            accs = BankAccount.deserialize(self._id)
            if accs:
                for acc in accs:
                    if acc._id == self._id:
                        if acc._account_balance >= amount:
                            acc._account_balance -= amount
                            BankAccount.serialize(BankAccount._accounts)
                            return True
                        return False
                return False
            return False
        return False

    def display_balance(self):
        '''Deserializes `./accounts.db` file back into the python array'''
        '''Prints the account balance of account <self._account_balance>'''
        accs = BankAccount.deserialize(self._id)
        for acc in accs:
            if acc._id == self._id:
                acc._account_balance += amount
                print(f"Current Balance: $[{acc._account_balance}]")

    def serialize(obj, *args, **kwargs):
        '''Writes a Python object into a file (or string)'''
        filepath = f'{obj._id}.db'
        mode = 'wb'
        try:
            with open(filepath, mode) as file:
                pickle.dump(obj, file)
        except e as Exception:
            print("[ Exception ERROR ]: Probably filename already exists")

    def deserialize(id, *args, **kwargs):
        '''Reads/Loads serialized data into code as actual python objects'''
        filepath = f'{id}.db'
        mode = 'rb'
        try:
            with open(filepath, mode) as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"{filepath} file does not exist...\nDeserializing into an empty array")
            return []
        except EOFError:
            print(f"Reached the end of {filepath} file...\nDeserializing into an empty array")
            return []




"""
BankAccount._accounts = ["aza-1"]

aza = BankAccount(100) -> aza{
                                "_id": "1",
                                "_account_balance": 100
                            }
aza.withdraw(90) -> 
aza.deposit(200) -> 
"""

