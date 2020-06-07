''' Type your code here. '''

how_many_number = int(input())
list_number = []
for index in range(how_many_number):
    number = int(input())
    list_number.append(number)

threshold = int(input())

for index in list_number:
    if(index <= threshold):
        print(index)