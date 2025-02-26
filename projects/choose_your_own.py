name = input("Type your name")
print(f"Welcome , {name} to this adventure!")

answer = input("You are on a dirt road ,which way you wanna go? ").lower()

if answer == "left":
    answer = input("You come to a river , you can walk around it or swim across it type walk or swim ")
elif answer == "right":

    print()
else:
    print("Not a valid option.you lose")