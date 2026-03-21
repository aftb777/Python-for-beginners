# function = A block of reuseable code 
#          place () after he function name to invoke it

def happy_birthday(name,age):#position of parameters also matters
    print(f"Happy birthday {name} ")
    print(f"Your are {age} years old now")
    print()
    
happy_birthday("Bro",20)
happy_birthday("Steve",56)
happy_birthday("Joe",32)

#Return = statement used to end a function 
#         and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def sub(x,y):
    z = x - y
    return z

print(add(1,2))
print(sub(1,2))

#Default arguements = A default value for certain parameters 
#                     default is used when that arguements is omitted
#                     make your functions more flexible

# def net_price(list_price,discount,tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500 , 0 , 0.05))


def net_price(list_price,discount = 0,tax = 0.05):#default arguements (discout,tax)
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))


#Exercise

import time 
def count(end , start = 0):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("done")
    
count(10)

# keyword arguements = an arguements preceded by an identifier
#                     helps with readability
#                     order of arguements doesnt matter
#                     1. positional 2. default 3. keyword 4. arbitrary

def hello(greeting , title , first , last):
    print(f"{greeting} {title} {first} {last}")
    
hello("Hello" , "Mr." , "spongebob" , "square pants")

hello("Hello" , title= "Mr." , last= "squarepants" , first= "spongebob")#Keyword arguements

for x in range(1 ,11):
    print(x , end = " ")
    
# Exercise : create a phone number 

def get_phone(country , area , first , last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country = 1 , area = 123 , first = 456 , last = 7890)

print(phone_num)

# *args = allows you to pass maultiple non-key arguements
# **kwargs = allows you to pass multiple keyword-arguements
#            * unpacking operator
#            1. positional 2. default 3. keywrod 4. arbitrary

def sum(*args):#we can also change parameters for ex *num (this is also an *args)
    total = 0
    for arg in args:
        total += arg
    return total
            
print(sum(4,2))

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

print_address(street = "123" , city= "Detroit" , state = "MI")

#Exercise : shipping label

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    for value in kwargs.values():
        print(value,end=" ")
        
    print(f"{kwargs.get('street')}")#print key value of street

shipping_label("Dr" , "spongebob" , "squarepants"
               , street = "123",
               apt = "100",
               city= "deteroit")