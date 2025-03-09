while True:
    
    operator = input("Enter an operator (+ - * /) or X to exit: ")

    if operator.lower() == 'x':
        print("Exiting the calculator. Goodbye!")
        break
    
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator. Please try again.")
        continue
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            result = "Error: Cannot be divided by 0"
    
    print("Result:", result)