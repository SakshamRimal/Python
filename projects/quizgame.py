print("Welcome to my computer quiz!  ")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("OKay! Let's play")
score = 0 

answer = input("What does cpu stands for? ")
if answer.lower() == "central processing unit":
    print("Wow ! correct answer")
    score += 1
else:
    print("Sorry! its not correct")

answer = input("What does gpu stands for? ")
if answer.lower() == "graphics processing unit":
    print("Wow ! correct answer")
    score += 1
else:
    print("Sorry! its not correct")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Wow ! correct answer")
    score += 1
else:
    print("Sorry! its not correct")

answer = input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Wow ! correct answer")
    score += 1
else:
    print("Sorry! its not correct")

print(f"Score : {score}")



 