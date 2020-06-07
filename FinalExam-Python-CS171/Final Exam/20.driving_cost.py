
def driving_cost(number_of_gallons, miles_per_gallon, dollars_per_gallon):
    cost = number_of_gallons * (dollars_per_gallon / miles_per_gallon)
    return cost

def readFloat(question):
    valid = False
    while not valid:
        try:
            x = input(question)
            x = float(x)
            if(x > 0):
                return x
        except ValueError as e:
            print('Not an float number. Try again.')

gallons = readFloat("Enter a number of gallons in tank: ")
fuel_efficiency = readFloat("Enter the fuel efficiency in miles per gallon: ")
price_per_gallons = readFloat("Enter the price of gas per gallon: ")
print("The cost per 100 miles is: %0.2f." %driving_cost(100, fuel_efficiency, price_per_gallons))
print("The car can go %0.2f miles with amount of gas is %0.2f." %(driving_cost(gallons, fuel_efficiency, price_per_gallons), gallons))