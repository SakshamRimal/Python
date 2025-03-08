class Bank:
    def __init__(self, account_id, account_name):
        self.account_id = account_id
        self.account_name = account_name
        self.balance = 0

    def new_account(self):
        print("Welcome to the bank!")
        print("Your account has been created successfully.")

    def close_account(self):
        print("Your account has been closed successfully.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. Remaining balance: {self.balance}")

    def deposit_money(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def display(self):
        print("Welcome:", self.account_name)
        print("Account ID:", self.account_id)
        print("Balance:", self.balance)

    def Menu(self):
        while True:
            print("\nPress 1 to open a bank account")
            print("Press 2 to close bank account")
            print("Press 3 to withdraw money from bank")
            print("Press 4 to deposit money into bank")
            print("Press 5 to display account details")
            print("Press X to exit")
            userInput = input("Enter your choice: ")
            if userInput == "1":
                self.new_account()
            elif userInput == "2":
                self.close_account()
            elif userInput == "3":
                self.withdraw()
            elif userInput == "4":
                self.deposit_money()
            elif userInput == "5":
                self.display()
            elif userInput.upper() == "X":
                print("Exiting...")
                break
            else:
                print("Invalid Input")

obj1 = Bank(1234, "Saksham")
obj1.Menu()
