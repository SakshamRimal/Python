# for value in range(1,5):
#     print(value)

# numbers = list(range(1,6))
# print(numbers)

# even_numbers = list(range(2,11,2))
# print(even_numbers)

# square = []
# for value in range(1,11):
#     squares = value**2
#     square.append(squares)  
# print(square)

# #------------list comprehension------------
# square = [i**2 for i in range(1,10)]
# print(square)

# words = ['hello','world', 'python']
# result = ''.join(words)
# print(result)

# word = ','.join([ i.upper() for i in words ])
# print(word)
# # join garyo bhane chai tyo array ko element lai linxa ani string ma convert garxa

# my_foods = ['pizza','falaferl','carrot cake']
# friend_foods = my_foods[:]
# print("My favourite foods are:")
# print(my_foods)
# print("My friends favorite foods are:")
# print(friend_foods)

# # yo chai without using the slice garyo bhane chai aliasing hunxa aba euta ma update gare arko ma ni copy bhainxa 
# my_foods = friend_foods
# my_foods.append("aalu")
# print(friend_foods)

# username = ['saks' ,' raks','maks','daks','admin']
# for i in range(0,len(username)):
#     if username[i] == "admin":
#         print("Hello admin,would you like to see a status report?")
#     else:
#         print(f"Hello {username[i]} thank you for login")
        
# Create lists of usernames
current_users = ['Ram', 'Shyam', 'Hari', 'Gita', 'Sita', 'Krishna']
new_users = ['Hari', 'gita', 'Laxmi', 'Shiva', 'Radha']

# Convert current_users to lowercase for case-insensitive comparison
# Using list comprehension to create a lowercase version
current_users_lower = [user.lower() for user in current_users]

# Loop through new_users to check availability
for new_user in new_users:
    # Convert new_user to lowercase for comparison
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. You will need to enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")