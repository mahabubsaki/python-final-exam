from datetime import datetime
class User:
    def __init__(self, name,bank, deposite=0,):
        self.name = name
        self.__balance = deposite
        bank.add_balance(deposite)
        self.transaction_history = []
        print(f"Account created for {name} with an initial deposit of ${deposite}.")
       
    def __repr__(self) -> str:
        return f'Account name {self.name} and current balance {self.__balance}'
    def deposit(self, amount,bank):
        if amount > 0:
            bank.add_balance(amount)
            self.__balance += amount
            self.transaction_history.append(f"Deposited ${amount} at {datetime.now().date()}")
        else:
            print("Deposite amount must be greater then 0")

    def withdraw(self, amount,bank):
        if amount <= 0:
            print("Withdraw amount must be greater then 0")
            return
        if self.__balance < amount:
            print("You can't withdraw more than your balance")
            return 
        if bank.is_bankrupt():
            print("the bank is bankrupt you can't withdraw money sorry")
            return
        self.__balance -= amount
        bank.withdraw_balance(amount)
        self.transaction_history.append(f"Withdrew ${amount} at {datetime.now().date()}")

    def check_balance(self):
        return self.__balance

    def transfer(self, recipient, amount):
        if amount <= 0:
            print("Withdraw amount must be greater then 0")
            return
        if self.__balance < amount:
            print("You can't transfer more than your balance")
            return
        self.__balance -= amount
        recipient.__balance += amount
        self.transaction_history.append(f"Transferred ${amount} to {recipient.name}")
        recipient.transaction_history.append(f'Recieved ${amount} from {self.name}')

    def check_transaction_history(self):
        return self.transaction_history

    def request_loan(self, bank,amount):
        if bank.loan_enabled:
            max_loan_amount = self.__balance * 2
            if(amount > max_loan_amount):
                print(f'{self.name} can not take more loan than twice of his balance')
                return
            self.__balance += amount
            bank.total_loan_amount += amount
            self.transaction_history.append(f"Requested and received a loan of ${amount}")
        else:
            print("Loan feature is currently disabled by the bank.")

