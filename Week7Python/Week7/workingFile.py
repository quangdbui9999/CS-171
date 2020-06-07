import sys
import os.path

print("Welcome to Book Analyzer v0.1")
fileName = input("Enter File Name to Read:\n")

try:
    file = open(fileName, "r")
    
    letter = input("Letter to search for:\n")
    if(len(letter) == 1):
        position = input("Enter Position (0 for first letter):\n")
        
        try:
            position = int(position)
            count = 0
            line = file.read()
            words = line.split()
            list_words = len(line.split())
            #s = words[2].lower()
            #print(s.find("e"))
            for i in range(0, list_words):
                if letter.lower() in words[i].lower():
                    temp_string = words[i].lower()
                    if temp_string.find(letter.lower(), position) == position:
                        count += 1
            print(f"There are {count} words with {letter} in position {position}")
        except ValueError as e:
            print('Error: A number is required.')
            sys.exit()
        
    else:
        print("Error: A single letter is required.")
        sys.exit()
    file.close()
except FileNotFoundError:
    print("Error: Could Not Open File.")
    sys.exit()