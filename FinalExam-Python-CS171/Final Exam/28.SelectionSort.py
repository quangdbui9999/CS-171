

import swapFunction

def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        smallest_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[smallest_index]:
                smallest_index = j
        swapFunction.swap(numbers, i, smallest_index)
        print(numbers)

array_numbers = [9, 0, 11, 10, 5, 8, 6, 7]
print("Selection Sort Input:", array_numbers)
selection_sort(array_numbers)
print("Result after Selection Sort:", array_numbers)