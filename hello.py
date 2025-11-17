

# Write a python program using while loop to create a simple banking system
balance = 0 #initial balance
running = True

print("Welcome to Simple Banking System!")

while running:
    print("\n--- MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4):")
    if choice == "1":
        print(f"Your current balance is: ${balance}")
        
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"${amount} deposited successfully! New balance: ${balance}")
        
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn successfully! New balance: ${balance}")
        else:
            print("Insufficient funds!")
            
    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        running = False
        
    else:
        print("Invalid choice! Please enter a number between 1 and 4.")




