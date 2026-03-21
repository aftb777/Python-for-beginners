# NOTE : print(help(str))
#above statement will give all string methods 

#Exersice:
# Validate user input 
# 1. username is no more than 12 characters 
# 2. Username must not conatin spaces
# 3. username must not contain digits

username = input("Enter a username : ")

if len(username) > 12:
    print("Your username cant be more than 12 characters")
    
elif not username.find(" ") == -1:
    print("Your username cant contain spaces")
    
elif not username.isalpha():
    print("Your username not contain numbers")
    
else: 
    print(f"welcome {username}")