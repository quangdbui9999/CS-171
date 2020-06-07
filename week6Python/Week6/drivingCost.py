''' Define your function here. '''

def readFloat(question):
    valid = False
    while not valid:
        try:
            x = input(question)
            x = float(x)
            return x
        except ValueError as e:
            print('Not an float number. Try again.')
            
def driving_cost2(miles_per_gallon, dollars_per_gallon):
    gas_cost_10 = (dollars_per_gallon / miles_per_gallon) * 10
    gas_cost_50 = (dollars_per_gallon / miles_per_gallon) * 50
    gas_cost_400 = (dollars_per_gallon / miles_per_gallon) * 400
    print("%0.2f\n%0.2f\n%0.2f" %(gas_cost_10, gas_cost_50, gas_cost_400))

def driving_cost(driven_miles, miles_per_gallon, dollars_per_gallon):
    cost = driven_miles * (dollars_per_gallon / miles_per_gallon)
    return cost
        

if __name__ == '__main__':
    ''' Type your code here. '''
    miles = ""
    if(miles != ""):
        miles = readFloat("")
        miles_gallon = readFloat("")
        dollars_gallon = readFloat("")
        print(f"{driving_cost(miles, miles_gallon, dollars_gallon)}")
    else:
        miles_gallon = readFloat("")
        dollars_gallon = readFloat("")
        driving_cost2(miles_gallon, dollars_gallon)
