import random

def main():
    random.seed(28)
    fileName = "randomNumber.txt"
    file = open(fileName, "w")
    for i in range (1, 1001):
        randNum = random.randint(1, 25)
        print(randNum)
        file.write(str(randNum))
        file.write("\n")
    file.close()

main()