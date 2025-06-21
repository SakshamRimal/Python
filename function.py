def greetUser():
    print("Hello!!")


def greeUser(username):
    print("Hello ," + username + "!") 
greeUser('joe')

def describe_pet(animal_type , pet_type):
    print("\nI have a " + animal_type +  ".")
    print("My" , animal_type + "'s name is " + pet_type + ".")

describe_pet('hamster','Harry')
    
def build_person(first_name , last_name):
    person = {'first':first_name , 'last': last_name}
    return person

musician = build_person('jimi' , 'hendrix')
print(musician)


# passing an arbitary number of arguments
# sometimes we dont have fixed number of arguments in the function so passing arbitary number of argumnent in done
# this is also known as args
# jati argument ni pass garna milne bhayo 
#args - arbitary arguments 

def make_pizza(*toppings):
 """Summarize the pizza we are about to make."""
 print("\nMaking a pizza with the following toppings:")
 for topping in toppings:
    print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
# aba esma chau hamle jati ni argument pathaina milne bhayp

# kwargs - keyword arguments 
def build_profile(first , last , **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key , value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)

# import pandas as pd
# pd bhaneko chai alias
# args - *args - yo bhaneko arbitary arguments
# kwars - **kwars - yo bhaneko chai keywords arguments
# aliasing bhaneko kunai ni memory location ko onject lai arko arko name dine 

list1 = [1,2,3]
list2 = list1
# now list 2 is alias of list 1
# if we modify any of the list other list get modified too
# to solve this we either use .copy or [:] 
