unit = input("Is this tempreature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the tempreature:"))
if unit.lower() == "c":
    temp = round((9 * temp) / 5 + 32 , 1)
    print(f"The temperature in Farenheit is: {temp}F") 
    
elif unit.lower() == "f":
    temp = round((temp - 32) * 5/9 , 1)
    print(f"The temperature in Celsius is: {temp}C") 
    
else:
    print(f"{unit} is an invalid unit of measurement")