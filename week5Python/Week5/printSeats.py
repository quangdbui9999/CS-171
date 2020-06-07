num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces


''' Your solution goes here '''
number = 1
while number<= num_rows:
    letter = 'A'
    i = 1
    while i <= num_cols:
        print("%d%s" %(number, letter), end = ' ')
        letter = chr(ord(letter) + 1)
        i += 1
    number += 1

print()