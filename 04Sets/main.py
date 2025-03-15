myset = {1,2,3,2,5}
# print(myset)
# set doesnot allow duplication so it will not print any duplicate values 

myset.add(1)
myset.add(6)
myset.add(2)
myset.discard(5)
myset.pop()

for i in myset:
    print(i)

print(myset)

myset1 = {5,6,3,2,6}

a = myset.union(myset1)
print(a)

b = myset.intersection(myset1)
print(b)

c = myset.difference(myset1)
print(c)

d = myset.update(myset1)
print(d)

e = myset.issubset(myset1)
print(e)