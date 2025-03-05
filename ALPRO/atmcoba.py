balance = 1000000

print("\n₊ ⊹₊ ⊹₊ ⊹₊ ⊹ Welcome to Holkay Bank ꒰ᐢ. .ᐢ꒱₊˚⊹˚")

nim = input("Enter NIM: ")
name = input("Enter Name: ")
bank_account = input("Enter Bank Account: ")

security_code = input("Enter 6-digit security code: ")

if security_code.isdigit() and len(security_code) == 6:
    print("\n₊ ⊹₊ ⊹₊ ⊹ PIN is valid ꒰ᐢ. .ᐢ꒱₊˚⊹ ")
else:
    print("\n₊ ⊹₊ ⊹₊ ⊹ Invalid PIN. Please enter a 6-digit number. (◞ ‸ ◟ㆀ) ")
    exit()

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        print(f"Your balance is Rp.{balance:,.2f}")

    elif choice == '2':
        amount = float(input("\nEnter withdrawal amount: "))
        if amount > balance:
            print("Insufficient funds")
        else:
            balance -= amount
            print(f"Withdrawal successful. Remaining balance: Rp.{balance:,.2f}")

    elif choice == '3':
        amount = float(input("\nEnter deposit amount: "))
        balance += amount
        print(f"Deposit successful. New balance: Rp.{balana :,.2f}")

    elif choice == '4':
        print("\n ⊹₊ ⊹₊ ⊹ Thanksfor banking with us. Goodbye! (ﾉ•ヮ•)ﾉ*:・ﾟ✧ ")
        break

    else:
        print(" ⊹₊ ⊹₊ ⊹ Invalid choice. Please enter a number between 1 and 4. ⊹₊ ⊹₊ ⊹ ")
