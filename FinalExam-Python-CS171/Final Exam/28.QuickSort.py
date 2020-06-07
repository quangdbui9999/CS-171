
import swapFunction


def partition(numbers, low, high):  
    pivot = numbers[(low + high) // 2]
    left = low
    right = high
    while True:
        while numbers[left] < pivot:
            left += 1

        while numbers[right] > pivot:
            right -= 1

        if left >= right:
            return right

        swapFunction.swap(numbers, left, right)
        print(f"Pivot number: {pivot}")
        print(numbers)


def quicksort(numbers, low, high):  
    if low < high:
        pivot = partition(numbers, low, high)
        quicksort(numbers, low, pivot)
        quicksort(numbers, pivot + 1, high)

#array_numbers = [9, 0, 11, 10, 5, 8, 6, 7]
array_numbers = [3,78,49,36,72,43,63]
print("Quick Sort Input:", array_numbers)
quicksort(array_numbers, 0, len(array_numbers) - 1)
print("Result after Quick Sort:", array_numbers)
