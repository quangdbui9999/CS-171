''' Type your code here. '''
import math

user_num = int(input())
x = int(input())
if x == 0:
    print("Error: Dividing by 0")
else:
    output1 = math.floor(user_num / x)
    output2 = math.floor(output1 / x)
    output3 = math.floor(output2 / x)
    output4 = math.floor(output3 / x)
    
    print('%.0f ' %output1, end = '')
    print('%.0f ' %output2, end = '')
    print('%.0f ' %output3, end = '')
    print('%.0f' %output4)