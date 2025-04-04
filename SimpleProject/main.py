resources={
    'water':500,
    'milk':200,
    'coffee':100,
}
is_one = True
while(is_one):
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice == 'off':
        is_one = False
    if choice == 'report':
        print(f"Water={resources['water']}ml")
        print(f"Water={resources['milk']}ml")
        print(f"Water={resources['coffee']}g")
        print(f"Water={resources['coffee']}g")
        
