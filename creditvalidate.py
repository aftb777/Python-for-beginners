# Pyhton credit card validator

# 1. remove any '-' or ' '
# 2. add all digits in the odd places from right to left 
# 3. Double every second digits from right to left
#      (if result is a 2-digit number, 
#       add the 2-digit number together to get a single digit)
# 4. sum the totals of step 2 & 3
# 5. If sum is divisible by 10, the credit card is valid

sum_odd_digits = 0
sum_even_digit = 0
total = 0

# Step 1 
card_number = input("Enter the credit card number : ")
card_number = card_number.replace("-","") 
card_number = card_number.replace(" ","")
card_number = card_number[::-1]
print(card_number)

# Step 2
for x in card_number[::-2]:
    sum_odd_digits = sum_even_digit + int(x)
    
# Step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digit += (1 + (x % 10))
    else:
        sum_even_digit += x
        
# Step 4
total = sum_even_digit + sum_odd_digits

# Step 5
if total % 10 == 0:
    print("Valid")
else:
    print("Inavlid")