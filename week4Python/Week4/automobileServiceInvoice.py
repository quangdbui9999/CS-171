# Type your code here

import sys
def getKeyList(myDictionany):
    return list(myDictionany.keys())
    
def output_services():
    print('Davy\'s auto shop services')
    print('Oil change -- $35')
    print('Tire rotation -- $19')
    print('Car wash -- $7')
    print('Car wax -- $12\n')

car_services = {
    'oil change': 35,
    'tire rotation': 19,
    'car wash': 7,
    'car wax': 12
}

output_services()

input_service1 = input('Select first service:\n')
input_service2 = input('Select second service:\n')

print('\nDavy\'s auto shop invoice\n')
price1 = 0
price2 = 0
for key in getKeyList(car_services):
    if(key == input_service1.lower()):
        price1 = car_services[key]
        print(f'Service 1: {input_service1}, ${price1}')
        
if(input_service1.lower() not in getKeyList(car_services)):
    print("Service 1: No service")
    
for key in getKeyList(car_services):
    if(key == input_service2.lower()):
        price2 = car_services[key]
        print(f'Service 2: {input_service2}, ${price2}')

if(input_service2.lower() not in getKeyList(car_services)):
    print("Service 2: No service")

total = price1 + price2

print(f'\nTotal: ${total}')