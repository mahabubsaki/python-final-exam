from bank import Bank
from admin import Admin
from users import User

def main():
    #bank creation
    bank = Bank(10000,True)
    #normal account creation
    user = User("Mahabub Saki","m@gmail.com","123",bank,5000)
    print(f'Banks Current balance before deposite is ${bank.check_bank_balance()}')
    #user is depositing on bank
    user.deposit(1000,bank)
    print(f'Banks Current balance before withdraw and after deposite is ${bank.check_bank_balance()}')
    #user is withdrawing on bank
    user.withdraw(3000,bank)
    print(f'Banks Current balance after withdraw is  ${bank.check_bank_balance()}')
    #user is cheking his/her transaction history
    print(user.transaction_history)
    #account creation by account
    admin = Admin()
    jack = admin.create_account(bank,"Jack","m@gmail.com","123",5000)
    print(f'Banks Current balance before deposite is ${bank.check_bank_balance()}')
    jack.deposit(5000,bank)
    print(f'Banks Current balance before withdraw and after deposite is ${bank.check_bank_balance()}')
    jack.withdraw(7000,bank)
    print(f'Banks Current balance after withdraw is  ${bank.check_bank_balance()}')
    print(jack.check_transaction_history())

    #jacks current balance is 3000 so he can't take more than 3000*2 = 6000
    print(f'Jacks current balance is ${jack.check_balance()}')

    jack.request_loan(bank,7000)

    #jack can take loan if he request less then 6000
    jack.request_loan(bank,5000)
    print(f'Jacks current balance after loan is ${jack.check_balance()}')

    
    sparrow = admin.create_account(bank,"Sparrow","m@gmail.com","123",8000)


    print(f'Jacks current before transfer money ${jack.check_balance()}')
    print(f'Sparrow current before transfer money ${sparrow.check_balance()}')

    jack.transfer(sparrow,2000)

    print(f'Jacks current after transfer money ${jack.check_balance()}')
    print(f'Sparrow current after transfer money ${sparrow.check_balance()}')
    print(sparrow.check_transaction_history())
    print(jack.check_transaction_history())


    #admin checking all users of banks
    print(bank.accounts)

    #admin checking banks balance
    print(f'admin checking balance before taking loan ${bank.check_bank_balance()}')

    #admin checking loan amount before taking loan
    print(f'admin checking loan amount before taking loan : ${bank.check_total_loan_amount()}')
    bank.take_loan(20000)
    print(f'admin checking loan amount after taking loan : ${bank.check_total_loan_amount()}')
    print(f'admin checking balance after taking loan ${bank.check_bank_balance()}')
    #admin is turning off loan feature of bank
    admin.toggle_loan_feature(bank,False)

    #now no user cant take loan now
    sparrow.request_loan(bank,1000)
    
    
    admin.toggle_loan_feature(bank,True)
    #now user can take loan
    sparrow.request_loan(bank,1000)

    #admin checking if bank is bankcrupt
    print(admin.check_is_bankrupt(bank))

    #bank is not bankrupt as balance is 44000

    bank.withdraw_balance(44000)

    print(bank.check_bank_balance())

    #after withdrawing bank is bankrupt
    print(admin.check_is_bankrupt(bank))

    #now no user can't withdraw money

    #jack have 6000 in account
    print(f'jack have a balance of ${jack.check_balance()}')

    #but he can't withdraw as bank is bankrupt

    jack.withdraw(500,bank)




if __name__ == '__main__':
    main()