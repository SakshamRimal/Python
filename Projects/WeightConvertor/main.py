
weight = float(input("Enter your weight: "))  
unit = input("Kg or pounds? (K or L): ")

if unit.lower() == "k":
    converted_weight = weight * 2.205 
    converted_unit = "Lbs."
elif unit.lower() == "l":
    converted_weight = weight / 2.205 
    converted_unit = "Kgs."
else:
    print(f"{unit} is not a valid unit.")
    exit()  


print(f"Your weight is: {converted_weight:.2f} {converted_unit}")