import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)
    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    try:
        amount = float(params[0])
    except IndexError:
        pass
    except NameError:
        print("[ INVALID ] Usage: python3 main-0.py <command>:<amount>")
        print("[ INVALID ] Commands: deposit, withdraw, display")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if self.account_balance < amount:
            print("Insufficient funds.")
        else:
            account.withdraw(amount)
            print(f"Withdrew: ${amount}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")


if __name__ == '__main__':
    main()
