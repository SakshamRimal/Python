class Dog:
    def __init__(self , name , age):
        self.name = name
        self.age = age 
    def sit(self):
        print(self.name.title() + " is now sitting")

obj1 = Dog("Tome"  , "14")
print(obj1.sit())
        

        
        