user_input = input()
hourly_temperature = user_input.split()

''' Your solution goes here '''
for i in hourly_temperature:
    if i != hourly_temperature[len(hourly_temperature) - 1]:
        print(str(i) + " -> ", end='')
    else:
        print(i + " ")