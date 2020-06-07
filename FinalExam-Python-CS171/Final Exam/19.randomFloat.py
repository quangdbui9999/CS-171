
import random

count_lesser_1 = 0
count_greater_100 = 0
between1And100 = 0
print("Result of random numbers:")
for i in range(0, 1000):
    x = random.uniform(1, 100)
    if(x < 1.0):
        count_lesser_1 += 1
    if (x > 100.0):
        count_greater_100 += 1
    if(1.0 <= x <= 100.0):
        between1And100 += 1
    print("%0.3f" %x)
print(f"Counter of number less than 1.0: {count_lesser_1}.")
print(f"Counter of number greatter than 100.0: {count_greater_100}.")
print(f"The number between 1 and 100 (counter): {between1And100}.")