
def mystery(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + mystery(num_list, start + 1, end)

list_numbers = [9, 0, 3, 2, 7, 6, 10, 8, 1, 4, 5]
total = mystery(list_numbers, 0, len(list_numbers) - 1)
print(f"Sum of the list is: {total}.")

'''
The recursive function will computer the sum of all numbers in the list
num_list
Base case:
    if start > end:
        return 0
Recursive case:
    return [start] + mystery(num_list, start + 1, end)

'''

