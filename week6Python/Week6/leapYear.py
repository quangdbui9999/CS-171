def input_int(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            return x
        except ValueError as e:
            print('Error about the datatype, it is not Integer number. Try again.')

def is_leap_year(user_year):
    if((user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0):
        return True
    else:
        return False


''' Define your function here. '''

if __name__ == '__main__':
    ''' Type your code here. Your code must call the function. '''
    what_year = input_int("")
    if(is_leap_year(what_year) == True):
        print(f"{what_year} is a leap year.")
    else:
        print(f"{what_year} is not a leap year.")