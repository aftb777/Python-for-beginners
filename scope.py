# variable scope = where variable is visible and accessible
# scope resoltuion = (LEGB) local -> Ebclosed -> Global -> built-in

def fun1():
    a = 1
    print(a)#variable a is local to function 1
    
def fun2():
    b = 2
    print(b)#variable b is local to function 2
  
a = 5#global variable
print(a)
  
fun1()
fun2()

# Enclosed Function : function inside the function

# Built-in functions

from math import e
def func3():
    print(e)

func3() #e=2.71
e = 3.14
print(e)
func3() # e = 3.14 value changes