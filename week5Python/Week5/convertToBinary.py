''' Type your code here. '''

decimal = int(input())
binary = ""
while decimal != 0:
    remainder = decimal % 2
    decimal //= 2
    binary += str(remainder)
print(binary)