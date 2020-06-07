import random

def printRocket():
    for num in range(10, -1, -1):
        print(num)
    print("  *")
    print(" ***")
    print("*****")
    print("*****")
    print("*****")
    print("*****")

def main():
    numCorrect = 0
    for x in range(5):
        num1 = random.randrange(1, 10)
        num2 = random.randrange(1, 10)
        answer = int(input(str(num1) + " + " + str(num2) + " = "))
        
        if answer == (num1 + num2):
            print("Congratulations! Your answer is correct!\n")
            numCorrect += 1
        else:
            print("Sorry, your answer is incorrect." ,end=" ")
            print("The correct answer is: " + str(num1 + num2))
            
    if numCorrect == 5:
        print("\nGreat Job! You answered the problems correctly!")
        printRocket()
    else:
        print("You answered:",numCorrect,"questions correctly.")
        print("Type again for a perfect score!")


main()
        
        