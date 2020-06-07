''' Define your function here '''
def is_list_even(my_list):
    all_even = False
    counter = 0
    for index in my_list:
        if index % 2 == 0:
            counter += 1
    if(counter == len(my_list)):
        all_even = True
    return all_even

def is_list_odd(my_list):
    all_odd = False
    counter = 0
    for index in my_list:
        if index % 2 == 1:
            counter += 1
    if(counter == len(my_list)):
        all_odd = True
    return all_odd

def input_int(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            return x
        except ValueError as e:
            print('Error about the datatype, it is not Integer number. Try again.')



if __name__ == '__main__':
    ''' Type your code here. '''

    num_list = input_int("")
    list_number = [int(input()) for x in range(0, num_list)]
    if is_list_even(list_number):
        print('all even')
    elif is_list_odd(list_number):
        print('all odd')
    else:
        print('not even or odd')