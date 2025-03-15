mylist = ["banana" , "cherry" , "apple"]
print(mylist)

mylist2 = list()
mylist2.append(5)
print(mylist2)

item = mylist[-1]
print(item)

for i in  mylist:
    print(i)
    
if "banana" in mylist:
    print("yes")
    
else:
    print("no")

mylist.insert(1 , 'blueberry')
print(mylist)

mylist.pop()
print(mylist)

mylist.remove('cherry')
print(mylist)

item = mylist.clear()
print(item)

mylist = [1,2,3,4,5,6,7,8,9]
a = mylist[1:5] # strating index and stopping index 
print(a)

