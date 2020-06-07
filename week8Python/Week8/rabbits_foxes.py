import math
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

def bunnies(rabbits, foxes, years):
    A = 0.04
    B = 0.0005
    G = 0.2
    S = 0.00005
    
    if(years == 0):
        list_pets = []
        list_pets.append(rabbits)
        list_pets.append(foxes)
        return list_pets
    else:
        rabbits_previous = rabbits
        foxes_previous = foxes
        rabbits = rabbits_previous + math.floor(rabbits_previous * (A - B * foxes_previous))
        foxes = foxes_previous - math.floor(foxes_previous * (G - S * rabbits_previous))
        return bunnies(rabbits, foxes, years - 1)


if __name__=="__main__":
    print("Welcome to Predator-Prey Model.")
    number_rabbits = input_int("Enter Initial Rabbit Population:\n")
    number_foxes = input_int("Enter Initial Fox Population:\n")
    number_year = input_int("Enter Number of Years to Simulate:\n")
    
    num_rabbits, num_foxes = bunnies(number_rabbits, number_foxes, number_year)
    
    print(f"After {number_year} years there will be {num_rabbits} rabbits.")
    print(f"After {number_year} years there will be {num_foxes} foxes.")


