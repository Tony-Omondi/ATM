class Account:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"KES {amount} deposited successfully.")
        else:
            print("Invalid deposit amount. Try again.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Try again.")
        else:
            self.balance -= amount
            print(f"KES {amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Your current balance is: KES {self.balance}")

def main():
    print("Welcome to Python ATM!")
    name = input("Please enter your name: ")
    initial_balance = float(input("Please enter your initial balance: "))
    
    # Creating the account
    account = Account(name, initial_balance)
    print("Account created successfully!")

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for using Python ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
