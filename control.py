#if = do some code only If condition is true
#     Else do something else

age = int(input("Enter your age : "))
  
if age >= 100:
    print("you are too old")
    
elif age >= 18 :
    print("You are now signed up")
    
elif age < 0:
    print("You have not borned yet")
  
else: 
    print("you are not eligible")
    
response = input("What you like? : ")
if response == "Y": #Use == for comparision 
    print("Have some food")
else:
    print("No food for you")
    
name = input("Enter your name : ")
if name == " ":
    print("You have not entered your name")
else: 
    print(f"hello {name}")
    
for_sale = True 

if for_sale:
    print("this item is for sale") 
else:
    print("This item is not for sale")