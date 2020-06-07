''' Type your code here. '''
list_number = []
number = int(input())
while(number > 0):
    list_number.append(number)
    number = int(input())

print(min(list_number), max(list_number))