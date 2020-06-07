import sys
validData = True

item_1 = input('Enter the cost of item_1:')

try:
    item_1 = float(item_1)
except ValueError as e:
    print('Value entered was not a number.')
    validData = False

if validData and item_1 < 0:
    print('Invalid data: item_1 is too low.')
    validData = False

item_2 = input('Enter the cost of item_2:')

try:
    item_2 = float(item_2)
except ValueError as e:
    print('Value entered was not a number.')
    validData = False

if validData and item_2 < 0:
    print('Invalid data: item_2 is too low.')
    validData = False

payment = input('Enter amount of payment: ')

try:
    payment = float(payment)
except ValueError as e:
    print('Value entered was not a number.')
    validData = False

if validData and payment < 0:
    print('Invalid data: payment is too low.')
    validData = False
    
if not validData :
    print('Invalid data.')
    sys.exit()
    
totalCost = item_1 + item_2
if(payment >= totalCost):
    print('Thank you.\nHere is your change: %.2f.' %(payment - totalCost))
else:
    print('You owned: %.2f' %(totalCost - payment))