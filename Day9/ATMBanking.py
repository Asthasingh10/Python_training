
# - Simulate an ATM system for checking balance, withdrawal, and deposit.
# - Use loops for multiple transactions and conditionals to prevent overdraft.

def atm_simulation():
    balance = 1000.0  
    print("🏦 Welcome to the Python ATM!")
    while True:
        print("\nChoose a transaction:")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print(f"💰 Your current balance is: ₹{balance:.2f}")

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("❌ Invalid amount. Please enter a positive number.")
            elif amount > balance:
                print("⚠️ Insufficient balance! Withdrawal denied.")
            else:
                balance -= amount
                print(f"✅ Withdrawal successful! New balance: ₹{balance:.2f}")

        elif choice == "3":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("❌ Invalid amount. Please enter a positive number.")
            else:
                balance += amount
                print(f"✅ Deposit successful! New balance: ₹{balance:.2f}")

        elif choice == "4":
            print("👋 Thank you for using the Python ATM. Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option (1-4).")

atm_simulation()
