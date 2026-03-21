import datetime

name = input("Enter your name : ")
x = input("Enter DOB (dd/mm/yyyy) : ")
curr = datetime.datetime.now()

y = x[6] + x[7] + x[8] + x[9]
age = curr.year - int(y)
print(f"Your current age is {age}")

if age<=60:
    print("You are not senior citizen")

else:
    print("you are senior citizen")
    
# def calculate_age(birth_year, birth_month, birth_date):
#     today = date.today()
#     age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_date))
#     return age

# def is_senior(age):
#     age >= 60
    
    
# birth_year = int(input("Enter birth year : "))
# birth_month = int(input("Enter birth month : "))
# birth_date = int(input("Enter birth date : "))

# age = calculate_age(birth_year, birth_month, birth_date)

# print(f"You are {age} years old")
# if is_senior(age):
#     print("You are senior citizen")
# else:
#     print("You are not senior citizen")