letter = input("Enter a letter from 'a' to 'z': ")
while(len(letter) != 1 or (letter < 'a' or letter > 'z')):
    print(letter + " is invalid letter.")
    if(len(letter) != 1):
        print("You should enter a letter")
    letter = input("Enter a letter from 'a' to 'z', please: ")
print("You enter a letter %s." %letter)