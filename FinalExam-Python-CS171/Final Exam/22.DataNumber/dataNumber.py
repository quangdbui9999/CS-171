
# Initialize some ramdom integer number
'''
import random

fileName = "data.txt"
fileOut = open(fileName, 'w')
count = 0
for i in range (0, 300):
    x = random.randint(-100, 100)
    if(x == 0):
        count += 1
    print(x)
    fileOut.write(str(x) + "\n")
print(f"Random number 0 is: {count}")
fileOut.close()
'''

def getData(fileName):
    myFile = open(fileName, 'r')
    content = myFile.readlines()

    number_positive = 0
    number_negative = 0

    list_positive = []
    list_negative = []

    for line in content:
        number = int(line)
        if number > 0:
            number_positive += 1
            list_positive.append(number)
        if number < 0:
            number_negative += 1
            list_negative.append(number)
            
    print(f"Number positive: {number_positive}\nNumber negative: {number_negative}")
    print(f"Positive numbers: {list_positive}")
    print(f"Negative numbers: {list_negative}")
    myFile.close()
    return (list_positive, list_negative)

def writeData(fileName, what_list):
    fileOut = open(fileName, 'w')
    for i in what_list:
        fileOut.write(str(i) + "\n")
    print(f"Writing file '{fileName}' succesfully")
    fileOut.close()
    
nameOfFile = "data.txt"
positive_list, negative_list = getData(nameOfFile)

writeData("dataplus.txt", positive_list)
writeData("dataminus.txt", negative_list)