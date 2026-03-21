operator = input("Enter an operator : ")
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number : "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)
    
elif operator == "*":
    print(num1 * num2)
    
elif operator == "/":
    if num2 == 0:
        print("Infinity") 
    else:
        print(num1/num2)
    
else :
    print("Invalid operator")  