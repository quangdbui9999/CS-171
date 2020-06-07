import sys
validData = True

testA = input('Enter the testA: ')

try:
    testA = int(testA)
except ValueError as e:
    print('Value entered was not a number.')
    validData = False

if not validData :
    print('Invalid data.')
    sys.exit()
num1 = 0
if testA == 25:
    num1 += 5
    print(f'num1 = {num1}')
else:
    num1 -= 5
    print(f'num1 = {num1}')