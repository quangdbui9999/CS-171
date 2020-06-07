''' Type your code here. '''
#from decimal import *

#getcontext().prec = 3


cars_miles_per_gallon = float(input())
gas_dollars_per_gallow = float(input())

gas_cost_10 = (gas_dollars_per_gallow / cars_miles_per_gallon) * 10;
gas_cost_50 = (gas_dollars_per_gallow / cars_miles_per_gallon) * 50;
gas_cost_400 = (gas_dollars_per_gallow / cars_miles_per_gallon) * 400;

print("%0.2f %0.2f %0.2f" %(gas_cost_10, gas_cost_50, gas_cost_400))