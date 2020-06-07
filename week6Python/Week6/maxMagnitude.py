import math

''' Define your function here. '''
def max_magnitude(user_val1, user_val2):
    max = 0
    if abs(user_val1) >= abs(user_val2):
        max = user_val1
    else:
        max = user_val2
    return max

if __name__ == '__main__':
    ''' Type your code here. '''
    first_number = int(input())
    second_number = int(input())
    print(max_magnitude(first_number, second_number))
