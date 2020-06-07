input_month = input()
input_day = int(input())

''' Type your code here. '''
if(input_month.lower() == 'march' and 20 <= input_day <= 31) or (input_month.lower() == 'april' and 1 <= input_day <= 30) or (input_month.lower() == 'may' and 1 <= input_day <= 31) or (input_month.lower() == 'june' and 1 <= input_day <= 20):
    print('spring')
elif(input_month.lower() == 'june' and 21 <= input_day <= 30) or (input_month.lower() == 'jyly' and 1 <= input_day <= 31) or (input_month.lower() == 'august' and 1 <= input_day <= 31) or (input_month.lower() == 'september' and 1 <= input_day <= 21):
    print('summer')
elif(input_month.lower() == 'september' and 22 <= input_day <= 30) or (input_month.lower() == 'october' and 1 <= input_day <= 30) or (input_month.lower() == 'november' and 1 <= input_day <= 31) or (input_month.lower() == 'december' and 1 <= input_day <= 20):
    print('autumn')
elif(input_month.lower() == 'december' and 21 <= input_day <= 31) or (input_month.lower() == 'january' and 1 <= input_day <= 31) or (input_month.lower() == 'february' and 1 <= input_day <= 28) or (input_month.lower() == 'march' and 1 <= input_day <= 19):
    print('winter')
else:
    print('invalid')