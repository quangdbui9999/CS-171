
import random

number_even = 0
number_odd = 0

for i in range(0, 100):
    x = random.randint(1, 999)
    if(x % 2 == 0):
        number_even += 1
    else:
        number_odd += 1
print(f"Numbers of even numbers are {number_even}.")
print(f"Numbers of odd numbers are: {number_odd}.")