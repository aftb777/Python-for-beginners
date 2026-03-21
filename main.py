a = input("Enter first number : ")
b = input("Enter second number : ")
op = input("Enter the operator : ")    

if(op == "+"):
    print(int(a)+int(b))
    
elif(op == "-"):
    print(int(a)-int(b))
    
elif(op == "*"):
    print(int(a)*int(b))
    
elif(op == "/"):
    print(int(a)/(b))
    
else:
    print("Invalid operator")
    
# match op:
#     case "+":
#         print(int(a) + int(b))
        
#     case "-":
#         print(int(a) - int(b))
        
#     case "*":
#         print(int(a) * int(b))
        
#     case "/":
#         print(int(a) / int(b))
        
#     case _:
#         print("Invalid Operator")

# w = input("Enter the number : ")
# for x in range(1,int(w)):
#     if(x%2 == 0):
#         print(x)
#     if(x>int(w)):
#         break

# import operator


# w = "Aftaab"
# v = "Mulla"

# x = operator.__add__(w,v)
# print(x)

# date = input("Enter your age : ")

# if int(date) >= 60:
#     print("Senior citizen")
    
# elif int(date) == 60:
#     print("Come next year")
    
# else:
#     print("Not a senior citizen")
# import string


# b = input("Enter the string : ")
# print("Reversed String : " + b[::-1])

# c = b.lower()
# print("Lowered String : " + c)

# d = b.upper()
# print("Uppered String : " + d)

# e = b.capitalize()
# print("Capitalized String : " + e)

# f = b.swapcase()
# print("Swapped Case : " + f)


# x=b.count("a")
# print(x)

# o= b.split()
# print(o)

# g = b.casefold()
# print("Casefold string : " + g)

# a =b.zfill(5)
# print(a)


# EXP 1 : calculator with if else and switch
# EXP 2 : string operations min 20