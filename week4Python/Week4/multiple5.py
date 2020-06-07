import sys
validData = True

number = input('Enter a number for multiple of 5 between 1 and 100: ')

try:
    number = int(number)
except ValueError as e:
    print('Value entered was not a number.')
    validData = False

if validData and not(1 <= number <= 100):
    print('Invalid data.')
    validData = False

if not validData :
    print('Invalid data.')
    sys.exit()
    
if (number % 5 == 0):
    print(f'{number} is valid')
else:
    print(f'{number} is NOT valid')
    