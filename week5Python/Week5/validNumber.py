
number = int(input("Enter a number between 1 - 10 (inclusive): "))

while (number < 1) or (number > 10):
    print("Invalid number")
    number = int(input("Enter a number between 1 - 10 (inclusive), please: "))
print("The number you are entered: %d." %number)