''' Type your code here. '''
number1 = int(input())
number2 = int(input())
number3 = int(input())
max = 0
if(number1 >= number2) and (number1 >= number3):
    max = number1
elif (number2 >= number1) and (number2 >= number3):
    max = number2
else:
    max = number3
print(f"{max}")