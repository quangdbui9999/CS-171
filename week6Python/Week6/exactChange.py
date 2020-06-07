''' Define your function here '''
def exact_change(user_total):
    amount_dollars = 0
    amount_quarters = 0
    amount_dimes = 0
    amount_nickels = 0
    amount_pennies = 0
    
    dollars = 100
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1
    while(user_total > 0):
        if(user_total >= dollars):
            amount_dollars = user_total / dollars
            user_total = user_total - (int(amount_dollars) * dollars)
        if(user_total >= quarters):
            amount_quarters = user_total / quarters
            user_total = user_total - (int(amount_quarters) * quarters)
        if(user_total >= dimes):
            amount_dimes = user_total / dimes
            user_total = user_total - (int(amount_dimes) * dimes)
        if(user_total >= nickels):
            amount_nickels = user_total / nickels
            user_total = user_total - (int(amount_nickels) * nickels)
        if(user_total >= pennies):
            amount_pennies = user_total / pennies
            user_total = user_total - (int(amount_pennies) * pennies)
    return (int(amount_dollars), int(amount_quarters), int(amount_dimes), int(amount_nickels), int(amount_pennies))



if __name__ == '__main__': 
    input_val = int(input())    
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
    if input_val <= 0:
        print("no change")
    elif input_val > 0:
        if num_dollars == 1:
            print(f"{num_dollars} dollar")
        elif num_dollars > 1:
            print(f"{num_dollars} dollars")
        if num_quarters == 1:
            print(f"{num_quarters} quarter")
        elif num_quarters > 1:
            print(f"{num_quarters} quarters")
        if num_dimes == 1:
            print(f"{num_dimes} dime")
        elif num_dimes > 1:
            print(f"{num_dimes} dimes")
        if num_nickels == 1:
            print(f"{num_nickels} nickel")
        elif num_nickels > 1:
            print(f"{num_nickels} nickels")
        if num_pennies == 1:
            print(f"{num_pennies} penny")
        elif num_pennies > 1:
            print(f"{num_pennies} pennies")

    ''' Type your code here. Your code must call the function. '''
