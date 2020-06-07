def main():
    fileName = "randomNumber.txt"
    file = open(fileName, "r")
    getSum = 0
    average = 0
    maxNumber = -1
    minNumber = 1000
    for i in range(0, 1000):
        line = file.readline()
        number = int(line)
        getSum += number
        
        if(number < minNumber):
            minNumber = number
        if(number > maxNumber):
            maxNumber = number
        
    average = float(getSum / 1000)
    print("Average is: " + str(average))
    print("Max number is : " + str(maxNumber))
    print("Min number is : " + str(minNumber))
    file.close()
    
main()