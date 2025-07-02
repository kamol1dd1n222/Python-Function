def deposit(balance, amount):
  if amount > 0:
        balance += amount
  return balance    

def withdraw(balance, amount):
  if amount <= balance:
       balance -= amount
  return balance     

def check_balance (balance):
     print(f"Balance: {balance}") 

hisob = 100
qoshish = int(input("Deposit:  "))
hisob = deposit(hisob, qoshish)
check_balance(hisob)
ayirish = int(input("Withdraw: "))
hisob = withdraw(hisob, ayirish)
check_balance(hisob)
