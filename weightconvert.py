weight = float(input("Enter your Weight : "))
unit = input("Kilogram or Pounds? (K or L):").upper()

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is : {weight} {unit}")
    
elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"your weight is : {weight} {unit}")
      
else:
    print(f"The {unit} is invalid")