# class Car:
#     name= "Nexon"
#     type = "suv"

# obj = Car()
# x = obj.name
# print(x)

class Atm:
    # j function banaye ni it is method
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
     while True: 
        user_input = input(""" 
        Hello, How would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit                  
                           """)     
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        elif user_input == '5':
            self.exit()
        else:
            print("Invalid input. Please try again.")

            

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin created sucessfully")
    
    def deposit(self):
        pin = input("Enter you pin ")
        if pin == self.pin:
             self.amount = int(input("Enter a amount you want to deposit "))
             self.balance = (self.balance) + (self.amount)
             print("Ammount Added Sucessfully")
        else:
            print("Incorrect pin ")
    
    def withdraw(self):
        if(self.balance == 0):
            print("Your Balance: 0")
        else:
             self.credit = int(input("Enter an amount you want to withdraw "))
             self.balance = self.amount - self.credit
             print(self.balance)
       
    def check_balance(self):
        pin = input("Enter your pin ")
        if pin == self.pin:
            print("Your balance: ",self.balance)
    
    def exit(self):
        enter = input("Enter X to exit ")
        if enter == 'X'.upper():
            exit()
        else:
            pass
    
obj = Atm()
obj1 = Atm()



    

    