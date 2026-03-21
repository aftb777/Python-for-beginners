unit = input("is this tempin Celsius or Farhenheit (C/F) : ").upper()
temp = float(input("Enter the temperature : "))

if unit == "C":
    temp = (9 * temp) / 5 + 32
    print(f"The temperature in Farheneit is : {temp}{unit}")

elif unit == "F":
    temp = (temp - 32) * 5 + 32
    print(f"The temperature in celsius is : {temp}{unit}")

else:
    print(f"{unit} is an invalid unit of mesurement")