#Indexing = accessing elements of a sequence using [] 
#Indexing operators [start :end : step]

credit_number = "1234-3444-5443-5677"

print(credit_number[0])

print(credit_number[0:4]) 
        #OR
#print(credit_number[:4])

print(credit_number[5:9])

print(credit_number[5:])#print from index 5 to last number 

#We can count by tables of 2,3,4,5.....

print(credit_number[::2])#print index divisible by 2

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

reverse_number = credit_number[::-1]#This will reverse the number
print(reverse_number)

# NOTE : We can also perform arithmatics on indexes