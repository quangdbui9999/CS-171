user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]
# 1 2 3, 4 5 6, 7 8 9
# 
#mult_table = [1]
for row in mult_table:
    for col in range(0, len(row)):
        if((col + 1) % len(row) != 0):
            print("%d | " %row[col], end='')
        else:
            print("%d" %row[col], end='')
        # print(col, end='') #index
    print()