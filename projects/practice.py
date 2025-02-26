# # # # # # print("Hello World")

# # # # # # name = input("Enter your name ").upper()
# # # # # # print("Hello %s"%name)

# # # # # # x = float(2.0)
# # # # # # print(x)
# # # # # # y = int(2)
# # # # # # print(x)

# # # # # # print(bool())
# # # # # # z = 0
# # # # # # if z == 0:
# # # # # #     print(bool(z))

# # # # # # x = 1
# # # # # # y = 2 

# # # # # # x = x + y
# # # # # # y = x - y
# # # # # # x = x - y

# # # # # # print(x)
# # # # # # print(y)

# # # # # x = int(input("Enter a number"))
# # # # # y = int(input("Enter a number"))

# # # # # while(True):
# # # # #     choice = int(input("1)For sum press 1 \n2)For difference press 2 \n3)For product press 3 \n"))
# # # # #     if(choice == 1):
# # # # #         add = x + y
# # # # #         print("Addtion: %d"%add)
# # # # #         break
# # # # #     elif(choice == 2):
# # # # #         if ( x > y):
# # # # #             difference = x - y
# # # # #             print("Difference %d" %difference)
# # # # #         else:
# # # # #             difference = y - x
# # # # #             print("Difference %d" %difference)
# # # # #         break

# # # # #     elif(choice == 3):
# # # # #         product = x * y
# # # # #         print("Addtion: %d"%product)
# # # # #         break

# # # # # my_list = [1,2,3,4,5]
# # # # # print(my_list[1:5:3])

# # # # # my_list.append(6)
# # # # # my_list.append(7)
# # # # # print(my_list)
# # # # # my_list.pop()
# # # # # print(my_list)
# # # # # print(len(my_list))

# # # # # for x in range(5):
# # # # #     print(x)
# # # # # count = 0 
# # # # # while True:
# # # # #     print(count)
# # # # #     count += 1
# # # # #     if count > 5:
# # # # #         break

# # # # for x in range(10):
# # # #     if x % 2 != 0:
# # # #         print(x)
  

    

# # # numbers = [
# # #     951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
# # #     615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
# # #     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
# # #     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
# # #     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
# # #     958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
# # #     743, 527
# # # ]

# # # # your code goes here
# # # for number in numbers:
# # #     if number % 2 == 0:
# # #       print(number)
# # #     if number >= 237:
# # #       break


# # for i in range (1 , 11):
# #     print(i)

# # for i in range(1,21):
# #     if i % 2 == 0:
# #         print("Even number- %d"%i)


# # for i in range (1,11):
# #     mul = i * i
# #     print( i ,"*", i ,"=", mul  )

# # sum = 0
# # for i in range (1,51):
# #     sum = sum + i
# # print("Sum: %d"%sum)

# # for i in range (1,6):
# #     for j in range(1 ,i+1):
# #         print("*" ,end=" ")
# #     print()

# # my_string = "hello"
# # print(my_string[::-1])

# # my_string = "hello"
# # reversed_str = " "
# # for i in my_string:
# #     reversed_str = i + reversed_str
# # print(reversed_str)

# # def my_function():
# #     print("Hello from my function ")
# # my_function()

# # def my_function_with_args(username , greetings):
# #     print("Hello, %s, from my function , i wish you %s"%(username , greetings))

# # my_function_with_args("Alice","Goodmorning")


# # def my_function():
# #     print("Hello from my function!")

# # def my_function_with_args(username , greetings):
# #     print("Hello, %s, From my Function!, I wish you %s" %(username,greetings))

# # def sum_two_number(a ,b):
# #     return a + b 

# # my_function()

# # my_function_with_args("Saksham","Goodmorning")

# # print("Sum: %d"%sum_two_number(2,3))


# def greet(name , message = "Goodmorning!"):
#     print(f"{name},{message}")

# greet("Bob")
# greet("Alice" ,"Goodnight")


class Atm:
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
            try:
                user_input = int(user_input)  # Convert input to integer
                if user_input == 1:
                    self.create_pin()
                elif user_input == 2:
                    self.deposit()
                elif user_input == 3:
                    self.withdraw()
                elif user_input == 4:
                    self.check_balance()
                elif user_input == 5:
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

    def create_pin(self):
        self.pin = input("Enter a new PIN: ")
        print("PIN created successfully!")

    def deposit(self):
        if self.verify_pin():
            amount = float(input("Enter the amount to deposit: "))
            if amount > 0:
                self.balance += amount
                print(f"₹{amount} deposited successfully. New balance: ₹{self.balance}")
            else:
                print("Deposit amount must be positive.")

    def withdraw(self):
        if self.verify_pin():
            amount = float(input("Enter the amount to withdraw: "))
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{self.balance}")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                print("Withdrawal amount must be positive.")

    def check_balance(self):
        if self.verify_pin():
            print(f"Your current balance is: ₹{self.balance}")

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("Incorrect PIN. Please try again.")
            return False


# Create an ATM object
obj = Atm()
