# sort() method = used with lists (built i method for lists)
# sort() function = used with iterables 

# students = ["Squidward" , "Sandy" , "Patrik" , "Spongebob"]

# students.sort()# arrange in alphabetical order

# # students.sort(reverse = True) # arrange in alphabetical order from back

# for i in students:
#     print(i)
    
# print()

# student = ("Squidward" , "Sandy" , "Patrik" , "Spongebob")

# # use same reverse = true for reversing

# sorted_student = sorted(students)
# for x in sorted_student:
#     print(x)
    
# Exercise : sort list of tuples , sort it by Alphabts and numbers

students = [("Squidward" , "F" , 60) , 
        ("Sandy" , "A" , 33) ,
        ("Patrick" , "D" , 36), 
        ("Spongebob" , "B" , 20) , 
        ("Mr. Krabs" , "C" , 78)]

grade = lambda grades : grades[1] # All the alphabets in tuples are at index 1
mark = lambda marks : marks[2]
students.sort(key= grade) # use reverse = True for reversing
students.sort(key= mark)

for i in students:
    print(i)
    
print()
    
for marks in students:
    print(marks)
    
print()

for marks in students:
    print(marks)