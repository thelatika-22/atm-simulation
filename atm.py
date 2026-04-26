transactions=[]

#MAIN FUNCTION
def main():
    if authenticate():
        show_menu()

#AUTHENTICATE FUNCTION
def authenticate():
    user_pin=1234
    attempt=0
    while attempt<3:
        entered_pin=int(input("Enter PIN:"))
        if entered_pin==user_pin:
            print("\nAccess Granted")
            return True
        else:
            print("Incorrect Pin")
            attempt=attempt+1
    print("\nAttempts exceeded. Card Blocked")
    return False

#CHECK BALANCE FUNCTION
balance=1000
def check_balance():
    print("\nCurrent balance:",balance)

#DEPOSIT FUNCTION
def deposit():
    global balance
    amount=int(input("Enter Amount:"))
    if amount>0:
        balance=balance+amount
        transactions.append(("deposit",amount,balance))
        print("\nTransaction Successful")
    else:
        print("\nInvalid Transaction")
    return balance

#WITHDRAW FUNCTION
def withdraw():
    global balance
    amount=int(input("Enter Amount:"))

    if amount<=0:
        print("\nInvalid Amount")
    elif amount<=balance:
        balance=balance-amount
        transactions.append(("withdraw",amount,balance))
        print("\nWithdrawal Successful. Please Collect Your Cash")
    else:
        print("\nInsufficient Balance")
    return balance

#TRANSACTION HISTORY
def transaction_history():
    if len(transactions)==0:
        print("\nNo Transactions")
    else:
        print("\n---TRANSACTION HISTORY---")
        for t in transactions[-2:]:
            print("Type:",t[0].capitalize())
            print("Amount: Rs",t[1])
            print("Available Balance: Rs",t[2])
            print("------------------------")

#MENU FUNCTION
def show_menu():
    while True:
        print("\nMENU")
        print("1.Check Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Transaction History")
        print("5.Exit")

        choice=int(input("\nEnter Your Choice:"))

        if choice==1:
            check_balance()
        elif choice==2:
            deposit()
        elif choice==3:
            withdraw()
        elif choice==4:
            transaction_history()
        elif choice==5:
            print("Thank You for using the ATM.")
            print("Please take your Card")
            break
        else:
            print("Invalid Choice. Please Try Again!")
        
main()