is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''

def checkLeapYear(year):
    return ((year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)))
if(checkLeapYear(input_year)):
    print(f"{input_year} is a leap year.")
else:
    print(f"{input_year} is not a leap year.")