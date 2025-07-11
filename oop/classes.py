# class Dog():
#     def __init__(self , name , age ):
#         self.name = name 
#         self.age = age 
#     def sit(self):
#         print(self.name.title() + "is now sitting.")
#     def roll_over(self):
#         print(self.name.title() + "rolled over!")
# obj1 = Dog("Jack" , 14)
# obj1.sit()
# obj1.roll_over()

# obj2 = Dog("Willie" , 12)
# obj2.sit()
# obj2.roll_over()

class Restaurant():
    def __init__(self , restaurant_name , cuisine_type , number_served = 0):
        self.restaurant_name = restaurant_name 
        self.cuisine_type = cuisine_type
        self.number_served = number_served
    def describe_restaurant(self):
        print(f"Restaurant name : {self.restaurant_name} Cuisine_type: {self.cuisine_type}")
        print(f"Customer served: {self.increment_number_served()}")
    def open_restaurant(self):
        print("Restaurant is open")
    def increment_number_served(self):
        self.number_served = 5
        return self.number_served
        
obj1 = Restaurant("Trisara" , "Chinesse" , 2)
obj1.describe_restaurant()
obj1.open_restaurant()