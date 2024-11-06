from datetime import datetime

cash = 0

def get_current_datetime():
    now = datetime.now()
    return now.strftime("%d/%m/%Y"), now.strftime("%I:%M %p")

def buy_airtime():
    global cash
    amount = int(input("Enter amount: "))
    if amount <= cash:
        cash -= amount
        print(f"Airtime of {amount}. New balance is {cash}")
    else:
        print("Not enough balance for this transaction.")

def deposit():
    global cash
    amount = float(input("Enter amount: "))
    cash += amount
    print(f"Amount {amount} deposited successfully. New balance is: {cash}")

def send_money():
    global cash
    date, time = get_current_datetime()
    receiver = int(input("Enter the card number: "))
    amount = float(input("Enter amount: "))
    
    if 0 < amount <= cash:
        cash -= amount
        print(f"Amount {amount} was sent to {receiver} on {date} at {time}. New balance is: {cash}")
    else:
        print("Not enough money in your account.")

def withdraw_cash():
    global cash
    date, time = get_current_datetime()
    agent = int(input("Enter the agent number: "))
    amount = float(input("Enter amount: "))
    
    if 0 < amount <= cash:
        cash -= amount
        print(f"Amount of {amount} withdrawn successfully from agent {agent} on {date} at {time}. Balance is, {cash}")
    else: 
        print("Not enough money in your account.")

def pay_bill():
    global cash
    date, time = get_current_datetime()
    paybill = int(input("Enter the bill number: "))
    amount = float(input("Enter amount: "))
    
    if 0 < amount <= cash:
        cash -= amount
        print(f"Amount of {amount} paid to {paybill} on {date} at {time}. New balance is, {cash}")
    else: 
        print("Not enough money in your account.")

# Main program loop
while True:
    print("\nWelcome to the Geldautomat!")
    print("1.   Send Money")
    print("2.   Deposit Cash")
    print("3.   Withdraw Money")
    print("4.   Buy Airtime")
    print("5.   Pay Bill")
    
    try:
        user = int(input("Choose Option: "))
        
        if user == 1:
            send_money()
        elif user == 2:
            deposit()
        elif user == 3:
            withdraw_cash()
        elif user == 4:
            buy_airtime()
        elif user == 5:
            pay_bill()
        else:
            print("Make a valid request.")
    except ValueError:
        print("Invalid input. Please enter a number.")
