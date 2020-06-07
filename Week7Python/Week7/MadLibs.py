
import sys

print("Welcome to a fun word replacement game.")
fileName = input("Enter the name of the file to use:\n")

try:
    file = open(fileName, "r")
    words = file.read()
    open_brace = "["
    close_brace = "]"
    is_open_brace = False
    word_brace = ""
    result = ""
    vowels = ('a','e','i','o','u')

    for letter in words:
        if letter == open_brace:              
            is_open_brace = True
        elif letter == close_brace:
            is_open_brace = False
            
            magnitude_word_brace = len(word_brace)
            name = word_brace[1:magnitude_word_brace]
            holder = word_brace[1].lower()
            if holder in vowels:
                new_word = input("Please give an %s\n" %name)
            else:
                new_word = input("Please give a %s\n" %name)
            result += new_word
            
        if is_open_brace == False:
            if letter != ']':
                result += letter
            word_brace = ""
        else:
            if letter == '-':
                word_brace = word_brace + ' '
            else:
                word_brace = word_brace + letter
    
    print('Here is your story:')
    print('--------------------')
    print(result)
    file.close()
except FileNotFoundError:
    print("Error Bad File Name")
    sys.exit()