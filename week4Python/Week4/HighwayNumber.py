highway_number = int(input())

''' Type your code here. '''
if(highway_number == 0):
    print(f'{highway_number} is not a valid interstate highway number.')
if(1 <= highway_number <= 999):
    if(1 <= highway_number <= 99):
        if(highway_number % 2 == 0):
            print(f'The {highway_number} is primary, going east/west.')
        else:
            print(f'The {highway_number} is primary, going north/south.')
    if(100 <= highway_number <= 999):
        if(highway_number % 2 == 0):
            print(f'The {highway_number} is auxiliary, serving the {highway_number % 100}, going east/west.')
        else:
            print(f'The {highway_number} is auxiliary, serving the {highway_number % 100}, going north/south.')
if(highway_number >= 1000):
    print(f'{highway_number} is not a valid interstate highway number.')