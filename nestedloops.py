#nested loop = A loop within another loop (outer , inner)
#              outer loop:
#                  inner loop:

# for x in range(3):
#     for y in range(1,10):
#         print(y, end = " ")
#     print()

#Exercise : patterns 
rows = int(input("Enter the number of rows : "))
column = int(input("Enter the number of columns : "))

symbol = input("Enter a symbol to use : ")

for x in range(rows):
    for y in range(column):
        print(symbol, end = "")