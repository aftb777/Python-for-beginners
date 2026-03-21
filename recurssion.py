# recurrsion = function that call itself from within
#              helps to visualize a complex problem into basic steps,
#              which can be solved more easily iteratively or recursively

# Iteravtive
def walk(steps):
    for step in range(1 , steps + 1):
        print(f"You take step {step}")

walk(10)

print()

# Recursive approach

def walk(steps):
    if steps == 0:
        return

    walk(steps - 1)
    print(f"You take step {steps}")
    
walk(10)

print()
#Factorial of function both iteratively and recursively

def fact(x):
    result = 1
    if x > 0:
        for y in range(1,x+1):
            result *= y
        return result
            
print(fact(5))
print()

def factorial(x):
    if x == 1 or x ==0:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("Enter the number : "))
print(factorial(x))