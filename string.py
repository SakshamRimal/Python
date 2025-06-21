# string 
string = ' python '
print(f"Before length of string {len(string)}")
print(f"After length of string {len(string.rstrip())}")
new_str = string.rstrip()
left_strip = new_str.lstrip()
print(left_strip)

# lstrip and rstrip garera string ko white space haru strip garna milne bhayo

bicycle = ['one' , 'two' , 'three' , 'four']
print(f"There are {bicycle[2]} cycle")


motorcycles = ['honda', 'yamaha', 'suzuki'] 
# esari aba first bata insert garna milne bhayoo list ma
motorcycles.insert(0 , 'ducati') 
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.reverse()
print(motorcycles)

print(len(motorcycles))

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
    
magician = ['alice' , 'david'  , 'calorina']
magicians= (",").join([char for char in magicians])
print(magicians)
magicians = magicians.split(",")
print(magicians)