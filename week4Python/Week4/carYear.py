car_year = int(input())

''' Your solution goes here '''
if car_year <= 1969:
    print("Few safety features.")
if car_year >= 1970:
    print("Probably has seat belts.")
if car_year >= 1990:
    print("Probably has antilock brakes.")
if car_year >= 2000:
    print("Probably has airbags.")