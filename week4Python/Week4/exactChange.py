''' Type your code here. '''
money = int(input())

dollars = 100
quaters = 25
dimes = 10
nickels = 5
pennies = 1
amount_dollars = 0
amount_quarters = 0
amount_dimes = 0
amount_nickels = 0
amount_pennies = 0
remain = 0

if(money <= 0):
    print('no change')
if(money > 0):
    if(money >= dollars):
        amount_dollars = money / dollars
        money = money - (int(amount_dollars) * dollars)
        if(int(amount_dollars) == 1):
            print('%d dollar' %amount_dollars)
        elif(int(amount_dollars) > 1):
            print('%d dollars' %amount_dollars)
    if(money >= quaters):
        amount_quarters = money / quaters
        money = money - (int(amount_quarters) * quaters)
        if(int(amount_quarters) == 1):
            print('%d quarter' %amount_quarters)
        elif(int(amount_quarters) > 1):
            print('%d quarters' %amount_quarters)
    if(money >= dimes):
        amount_dimes = money / dimes
        money = money - (int(amount_dimes) * dimes)
        if(int(amount_dimes) == 1):
            print('%d dime' %amount_dimes)
        elif(int(amount_dimes) > 1):
            print('%d dimes' %amount_dimes)
    if(money >= nickels):
        amount_nickels = money / nickels
        money = money - (int(amount_nickels) * nickels)
        if(int(amount_nickels) == 1):
            print('%d nickel' %amount_nickels)
        elif(int(amount_nickels) > 1):
            print('%d nickels' %amount_nickels)
    if(money >= pennies):
        amount_pennies = money / pennies
        money = money - (int(amount_pennies) * pennies)
        if(int(amount_pennies) == 1):
            print('%d penny' %amount_pennies)
        elif(int(amount_pennies) > 1):
            print('%d pennies' %amount_pennies)