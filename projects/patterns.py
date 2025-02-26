
for i in range(1,6):
    for j in range(1,6):
        print("*" , end=" ")
    print()

print("------------------------------")

for i in range(1,6):
    for j in range (1 , i+1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for j in range (1 , i+1):
        print("*",end=" ")
    print()
for i in range(1,4):
    print("*")

print("------------------------------")

for i in range(1,6):
    for j in range (i , 6):
        print("*",end=" ")
    print()

for i in range(5 , 0 , -1):
    for j in range(i):
        print("*" ,end=' ')
    print()
print('------------------------------')

for i in range(1,6):
    for j in range (1 , i+1):
        print(j ,end=" ")
    print()

print('-------------------------------')

for i in range(5, 0, -1):
    for j in range(i , 0 ,-1):
        print(j , end=" ")
    print()

print("------------------------")
for i in range(1,6):
    print(" " * (5-i),end="")
    for j in range(1 ,i+1):
        print(j , end=" ")
    print()



