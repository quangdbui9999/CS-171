
def FahrenheittoCelcius(fahrenheit):
    celcius = (fahrenheit - 32) * (5 / 9)
    print("Convert %.2f to Celcius: %.2f. (Version 1)" %(fahrenheit, celcius))


def FahrenheittoCelcius_V2(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# Calling function
degree_F = 71
FahrenheittoCelcius(degree_F)
print("Convert %.2f to Celcius: %.2f. (Version 2)" %(degree_F, FahrenheittoCelcius_V2(degree_F)))


print("------------------------------------------")
print("|     Fahrenheit      |      Celcius     |")
print("------------------------------------------")
for counter in range(-30, 101, 10):
    print("|       %6.2f        |      %6.2f      |" %(counter, FahrenheittoCelcius_V2(counter)))
    print("------------------------------------------")
print("|           THE END OF PROGRAM           |")
print("------------------------------------------")
