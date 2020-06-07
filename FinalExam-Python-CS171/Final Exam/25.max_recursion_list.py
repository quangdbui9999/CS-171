
def get_max(x, y):
    if(x >= y):
        return x
    else:
        return y

def maxNumber(list_num, size_list):
    if(size_list == 1):
        return list_num[0]
    else:
        return get_max(list_num[size_list - 1], maxNumber(list_num, size_list - 1))

list_numbers1 = [9, 0, 3, 2, 7, 6, 10, 8]
list_numbers2 = [9, 0, 3, 2, 7, 6, 8, 11]
list_numbers3 = [12, 0, 3, 2, 7, 6, 9, 8]
print("Max number is: ", maxNumber(list_numbers1, len(list_numbers1)))
print("Max number is: ", maxNumber(list_numbers2, len(list_numbers2)))
print("Max number is: ", maxNumber(list_numbers3, len(list_numbers3)))
