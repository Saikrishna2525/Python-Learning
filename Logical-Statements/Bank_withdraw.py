# ● If balance is sufficient and amount is a multiple of 100 → Allow withdrawal and show remaining balance 
# ● If amount not multiple of 100 → "Amount must be in multiples of 100" ● If insufficient funds → "Insufficient balance" 

balance = 1000
withdraw_amount = int(input("How much money do you want to withdraw: "))

if withdraw_amount <= balance and withdraw_amount % 100 == 0:
    print(f"Amount withdrawal of rupees {withdraw_amount} is successful")
    balance -= withdraw_amount
    print(f"Current Balance: {balance}")
elif withdraw_amount % 100 != 0:
    print("Amount must be in multiples of 100")
else:
    print("Insufficient Funds!")
