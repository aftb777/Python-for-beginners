# zip(*iterables) = aggreagte elements from two or more iterables (lists , tuples ,sets)
#                  creates a zip object with paired elements stored in tuples for each elements

username = ["Dude" , "Bro" , "Mister"]
passwords = ("p@ssword" , "abc123" , "guest")

users = zip(username,passwords)

print(type(users))#we can also typecast the function into lists using list function

for i in users:
    print(i)
    
info = dict(zip(username,passwords))

for key , value in info.items():
    print(key+ " : "+value)