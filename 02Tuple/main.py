# it is same as list but the main difference between a tuple and a list is that it cannot be changed after its creation
# immutable 
# it is created with a paranthesis

mytuple = ("max", "")
print(type(mytuple))

# it is same as list but it cannot be changed this it is immutable 

for i in mytuple:
    if 'max' in mytuple:
      print(i)
    else:
        print("nothing")

print(mytuple.count('a'))

