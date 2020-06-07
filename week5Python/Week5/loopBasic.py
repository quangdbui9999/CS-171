name = input('Enter your name: ')
x = 0
while(x < 20):
    print(name)
    x = x + 1
print("The End.")

# -----------

number = int(input('Enter a number: '))
x = 1
while(x <= number):
    if(x % 10 == 0):
        print(x)
    else:
        print(x, end='')
    x = x + 1

# --------
number = 1
while(number <= 10):
    print(number)
    number = number + 1
#---------
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number, end= "  ")
    number = number + 1
    
#------
favorite = input('\nEnter your favorite ice cream flavor: ')
for x in range(1, 5):
    print(str(x) + '.', favorite, end = '\t')

