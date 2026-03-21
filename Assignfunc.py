def hello():
    print("Hello")
    
print(hello) # print memory address of the hello function

hi = hello

print(hi)# same memory address of hello
print()
hi()# print hello function

say = print
say("Hello world")
print()
 
# Higher order functions in Python 

# A function that either:
# 1. accepts a function as an arguement
#                or
# 2. returns a function 
# (In python , functions are also treated as object)

def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func("Hello")
    print(text)
    
hello(loud)
hello(quiet)

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)
print()
print(divide(10))