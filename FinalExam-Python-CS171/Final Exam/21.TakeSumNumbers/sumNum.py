
'''
import random

fileName = "number.txt"
fileOut = open(fileName, 'w')
count = 0
for i in range (0, 600):
    x = random.randint(0, 999)
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

    list_numbers = []

    for line in content:
        number = int(line)
        list_numbers.append(number)
            
    myFile.close()
    return list_numbers

if __name__ == "__main__":
    fileName = "number.txt"
    total = 0
    list_integer = getData(fileName)
    for i in list_integer:
        total += i
    print(f"Sum of the list numbers in file \"{fileName}\" is: {total}.")





