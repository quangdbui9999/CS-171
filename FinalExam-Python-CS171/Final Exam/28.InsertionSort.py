
import swapFunction

def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        j = i
        while j > 0 and numbers[j] < numbers[j - 1]:
            swapFunction.swap(numbers, j, j - 1)
            j -= 1
            print(numbers)

array_numbers = [9, 0, 11, 10, 5, 8, 6, 7]
print("Insertion Sort Input:", array_numbers)
insertion_sort(array_numbers)
print("Result after Insertion Sort:", array_numbers)
