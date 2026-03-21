# exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter the numerator : "))
    denominator = int(input("Entert the denominator : "))
    result = numerator /denominator

except ZeroDivisionError as e:#additional way to use e looks professional
    print(e)
    print("You cant divide by zero")
    
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
        
except Exception as e: #consider as good practise use Exeption at last
    print(e)
    print("Something went wrong :(")
    
else:
    print(result)
    
finally:
    print("This will always execute")