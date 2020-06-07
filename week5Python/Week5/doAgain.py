doAgain = 'y'
while doAgain == 'y':
    word = input("Enter a word: ")
    print("First letter of " + word + " is " + word[0])
    doAgain = input("Type 'y' to continue and anything else to quit.")
print("Done")