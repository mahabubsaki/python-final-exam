class Admin:
    @staticmethod
    def create_account(bank, user_name, initial_deposit):
       return bank.create_account(user_name, initial_deposit)

    @staticmethod
    def check_bank_balance(bank):
        return bank.check_bank_balance()

    @staticmethod
    def check_total_loan_amount(bank):
        return bank.check_total_loan_amount()

    @staticmethod
    def toggle_loan_feature(bank, enable):
        bank.toggle_loan_feature(enable)
    @staticmethod
    def check_is_bankrupt(bank):
       return "Yes" if bank.is_bankrupt() == True else "No"
       
