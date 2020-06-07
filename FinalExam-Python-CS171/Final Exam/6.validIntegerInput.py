
def input_int(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            if(x <= 0):
                print("The number should be positive number")
                valid = False
            else:
                return x
        except ValueError as e:
            print("The number is not a number.")
            valid = False

x = input_int("Enter a positive number: ")
print("You have entered a number: %d." % x)