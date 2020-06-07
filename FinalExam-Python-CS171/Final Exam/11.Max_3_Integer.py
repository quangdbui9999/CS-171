
def input_int(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            return x
        except ValueError as e:
            valid = False


def max_Integer(x, y, z):
    maxNumber = 0
    if(x > y and x > z):
        maxNumber = x
    elif(y > x and y > z):
        maxNumber = y
    else:
        maxNumber = z
    return maxNumber

first_number = input_int("Enter the first integer: ")
second_number = input_int("Enter the second integer: ")
third_number = input_int("Enter the third integer: ")
print(f'Max integer: {max_Integer(first_number, second_number, third_number)}')



