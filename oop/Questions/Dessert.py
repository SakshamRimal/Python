# A dessert shop is a specific type of restaurant. Write a class called DessertShop that inherits from the Restaurant class you wrote previously. Add an attribute called desserts that stores a list of dessert items available. Write a method called show_desserts() that prints all the desserts in the list. Create an instance of DessertShop with at least three dessert items and call the show_desserts() method.


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

class DessertShop(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,  desserts , number_served=0 ):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.desserts =list(desserts) 
    
    def show_desserts(self):
        print("-----Availabe Desserts------")
        for dessert in self.desserts:
            print(f"- {dessert}")
            

obj1 = DessertShop("Saksham" ,"Chinese" , ["Cake" , "Ice Cream" , "Brownie"])
obj1.describe_restaurant()
obj1.show_desserts()
obj1.open_restaurant()
        