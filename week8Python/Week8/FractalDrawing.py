import sys

def input_int(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            if(x < 0):
                valid = False
            else:
                return x
        except ValueError as e:
            valid = False

def fractal(length, spaces):
    if(length == 1):
        #print(' ' * spaces + '*')
        print(" " * spaces + "*")
    elif length > 1:
        fractal(int(length // 2), spaces)
        print(spaces * " " + length * "*")
        fractal(int(length // 2), spaces + int(length // 2))
        
'''
If length is 1 print out the number of spaces given followed by 1 star.
If the length is greater than one do the following:
Print the fractal pattern with half the length and the same number of spaces.
Print the number of spaces given followed by length stars.
Print the fractal pattern with half the length and spaces+(length//2) spaces in front of it.
'''

print("Fractal Generator")
number = input_int("Enter an integer > 0:\n")
fractal(number, 0)