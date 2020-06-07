user_input = input()
short_names = user_input.split()

''' Your solution goes here '''
short_names.pop(0)
short_names[len(short_names) - 1] = 'Joe'
print(short_names)