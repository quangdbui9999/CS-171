''' Type your code here. '''

def match_number(number):
    first_digit = int(number // 10)
    second_digit = int(number % 10)
    if first_digit == second_digit:
        return True
    else:
        return False

number = int(input())
if not(20 <= number <= 98):
    print("Input must be 20-98")
else:
    print(number)
    while(match_number(number) == False):
        number -= 1
        print(number)