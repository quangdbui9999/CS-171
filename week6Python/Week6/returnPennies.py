

''' Your solution goes here '''
def number_of_pennies(dollars, pennies = 0):
    return dollars * 100 + pennies

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only