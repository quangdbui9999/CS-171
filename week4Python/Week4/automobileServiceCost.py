# Type your code here
import sys
def getKeyList(myDictionany):
    return list(myDictionany.keys())

car_services = {
    'oil change': 35,
    'tire rotation': 19,
    'car wash': 7
}

input_services = input('Enter desired auto service:\n')

for key in getKeyList(car_services):
    if(key == input_services.lower()):
        print(f'You entered: {input_services}')
        print(f'Cost of {input_services.lower()}: ${car_services[key]}')
        #sys.exit()
if(input_services.lower() not in getKeyList(car_services)):
    print(f'You entered: {input_services}')
    print('Error: Requested service is not recognized')