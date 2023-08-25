from users import User
class Bank:
    def __init__(self,initial_balance,isLoanEnabled):
        self.accounts = []
        self.bank_balance = initial_balance
        self.loan_enabled = isLoanEnabled
        self.total_loan_amount = 0
        print(f'Bank is created with initial deposit of ${initial_balance}')

    def create_account(self, user_name, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit must be non-negative.")
            return
        account = User(user_name,self, initial_deposit)
        self.accounts.append(account)
        return account

    def check_bank_balance(self):
        return self.bank_balance

    def check_total_loan_amount(self):
        return self.total_loan_amount

    def toggle_loan_feature(self, enable):
        self.loan_enabled = enable
        status = "enabled" if enable else "disabled"
        print(f"Loan feature has been {status}.")
    def withdraw_balance(self,amount):
        if amount <= self.bank_balance:
            self.bank_balance -= amount
        else:
            print("Can't withdraw from bank more then amount")
    def add_balance(self,amount):
        self.bank_balance += amount
    def is_bankrupt(self):
        return self.bank_balance <= 0
    def take_loan(self,amount):
        if amount > 0:
            self.bank_balance += amount
            self.total_loan_amount += amount
        else:
            print("Loan amount must be greater than 0")
