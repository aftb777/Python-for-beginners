string = input("Enter the string : ")

print("Length:", len(string))

print("Uppercase:", string.upper())

print("Lowercase:", string.lower())

print("Contains 'World':", "World" in string)

print("Replace 'World' with 'Python':", string.replace("World", "Python"))

print("Split by comma:", string.split(","))

words = ["Hello", "Python"]
print("Join with space:", " ".join(words))

print("Starts with 'Hello':", string.startswith("Hello"))

print("Ends with '!':", string.endswith("!"))

print("Index of 'World':", string.find("World"))

print("Count of 'l':", string.count("l"))

whitespace_str = "  Hello, Python!  "
print("Trimmed:", whitespace_str.strip())

print("Is alphanumeric:", string.isalnum())

print("Is alphabetic:", string.isalpha())

num_str = "12345"
print("Is numeric:", num_str.isnumeric())

print("Repeat string 3 times:", string * 3)

print("Title case:", string.title())

name = "John"
age = 25
print("Formatted string:", f"My name is {name} and I am {age} years old.")

print("Reversed string:", string[::-1])

f = string.swapcase()
print("Swapped Case : " + f)