# # # # # # # # # # # # # def my_function():
# # # # # # # # # # # # #     print("Hello from my function ")
# # # # # # # # # # # # # my_function()

# # # # # # # # # # # # # def my_function_with_args(username , greetings):
# # # # # # # # # # # # #     print("Hello, %s, from my function , i wish you %s"%(username , greetings))

# # # # # # # # # # # # # my_function_with_args("Alice","Goodmorning")


# # # # # # # # # # # # # def my_function():
# # # # # # # # # # # # #     print("Hello from my function!")

# # # # # # # # # # # # # def my_function_with_args(username , greetings):
# # # # # # # # # # # # #     print("Hello, %s, From my Function!, I wish you %s" %(username,greetings))

# # # # # # # # # # # # # def sum_two_number(a ,b):
# # # # # # # # # # # # #     return a + b 

# # # # # # # # # # # # # my_function()

# # # # # # # # # # # # # my_function_with_args("Saksham","Goodmorning")

# # # # # # # # # # # # # print("Sum: %d"%sum_two_number(2,3))


# # # # # # # # # # # # # def greet(name , message = "Goodmorning!"):
# # # # # # # # # # # # #     print(f"{name},{message}")

# # # # # # # # # # # # # greet("Bob")
# # # # # # # # # # # # # greet("Alice" ,"Goodnight")

# # # # # # # # # # # # def greet(name , message="Goodmorning"):
# # # # # # # # # # # #     print(f"{name} , {message}")

# # # # # # # # # # # # greet("Bob")
# # # # # # # # # # # # greet("Bob","Goodnight")

# # # # # # # # # # # # print("------------------------")

# # # # # # # # # # # # def get_person_info():
# # # # # # # # # # # #     name ="Alice"
# # # # # # # # # # # #     age = 25
# # # # # # # # # # # #     location = "New York"
# # # # # # # # # # # #     return name , age ,location

# # # # # # # # # # # # info = get_person_info()
# # # # # # # # # # # # print(info)

# # # # # # # # # # # # print("-------------------------")

# # # # # # # # # # # # def factorial(n):
# # # # # # # # # # # #     if n == 0 or n == 1:
# # # # # # # # # # # #         return 1
# # # # # # # # # # # #     else:
# # # # # # # # # # # #         result = n * factorial(n - 1)
# # # # # # # # # # # #         print(f"factorial({n}) = {result}")  # Debugging intermediate results
# # # # # # # # # # # #         return result

# # # # # # # # # # # # fact = factorial(5)
# # # # # # # # # # # # print(f"Final Factorial: {fact}")

# # # # # # # # # # # # print("-------------------------")

# # # # # # # # # # # # def greet(name):
# # # # # # # # # # # #     print(f"Hello, {name}!")

# # # # # # # # # # # # def execute_function(greet, name):
# # # # # # # # # # # #     greet(name)

# # # # # # # # # # # # execute_function(greet, "Alice")

# # # # # # # # # # # def greet():
# # # # # # # # # # #     print("Hello World!!")
# # # # # # # # # # # greet()

# # # # # # # # # # # def add_numbers(a , b):
# # # # # # # # # # #     return a + b

# # # # # # # # # # # x = add_numbers(2,3)
# # # # # # # # # # # print("Sum : %d"%x)

# # # # # # # # # # # def introduce (name , age=18):
# # # # # # # # # # #     print("Hello, my name is %s and i am %d years old"%(name,age))
# # # # # # # # # # # introduce("Name")

# # # # # # # # # # # def square(x):
# # # # # # # # # # #     return x **2
# # # # # # # # # # # sqr = int(input("Enter a number"))
# # # # # # # # # # # y = square(sqr)
# # # # # # # # # # # print("Square: %d"%y)

# # # # # # # # # # def factorial(n):
# # # # # # # # # #     if n == 0 or n == 1:
# # # # # # # # # #         return 1
# # # # # # # # # #     else:
# # # # # # # # # #        return n * factorial(n-1)

# # # # # # # # # # x = factorial(5)
# # # # # # # # # # print(f"Factorial:{x} ")

# # # # # # # # # def fibonacci_recursive(n):
# # # # # # # # #     if n <= 0:
# # # # # # # # #         return 0
# # # # # # # # #     elif n == 1:
# # # # # # # # #         return 1
# # # # # # # # #     else:
# # # # # # # # #         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# # # # # # # # # # Generate the series
# # # # # # # # # def generate_fibonacci_series(n):
# # # # # # # # #     return [fibonacci_recursive(i) for i in range(n)]

# # # # # # # # # # Example usage
# # # # # # # # # n = int(input("Enter the number of terms: "))
# # # # # # # # # print(f"Fibonacci series for {n} terms: {generate_fibonacci_series(n)}")



# # # # # # # # import sys 
# # # # # # # # a = 'cdsbfdkjdkjbxc'
# # # # # # # # b = a
# # # # # # # # c = a
# # # # # # # # print(sys.getrefcount(a))




# # # # # # # def is_even(number):
# # # # # # #     """
# # # # # # #      this function tells if the given function is odd or even
# # # # # # #      input - any valid intger
# # # # # # #     """
# # # # # # #     if number % 2 == 0:
# # # # # # #         return "Even"
# # # # # # #     else:
# # # # # # #         return "Odd"
        
# # # # # # # for i in range(1,11):
# # # # # # #     print(" %s  is %s "%(i ,is_even(i)))

# # # # # # def func1(n):
# # # # # #     print(n +  "World")
  
# # # # # # def func2():
# # # # # #     func1("Hello ")

# # # # # # func2()

# # # # # # x = 10 
# # # # # # print(x)
# # # # # # print(type(x))

# # # # # x = 10
# # # # # y = 20

# # # # # x = x + y
# # # # # y = x - y
# # # # # x = x - y
# # # # # print(x)
# # # # # print(y)

# # # # x = 10.00
# # # # y = '20.00'
# # # # print("Before: %d"%x)
# # # # print("Before: %s"%y)

# # # # x = int(x)
# # # # print("After: %d"%x)
# # # # y = float(y)
# # # # print("After: %.2f"%y)


# # # my_list = [1,2,3,4,5]
# # # x = len(my_list)
# # # print("First element:", my_list[0])
# # # print("Last element:", my_list[x-1])

# # # my_list.append(6)
# # # print(my_list)

# # # my_list.pop()
# # # print(my_list)

# # # x = my_list[::-1]
# # # print(x)

# # my_list_1 = [4,2,6,3]
# # my_list_2 = [1,0,5,7]

# # new_list =( my_list_1 + my_list_2)

# # sorted_list = sorted(new_list)

# # print("MergedList:" ,new_list)
# # print("SortedList:" ,sorted_list)

# # Taking two numbers as input in one line
# num1, num2 = map(int, input("Enter two numbers separated by a space: ").split())

# # Printing the numbers
# print("First number:", num1)
# print("Second number:", num2







