def merge(values, i, j, k):
    merged_size = k - i + 1
    sorted_list = []        #Temporary list for merged values
    for x in range(merged_size):
        sorted_list.append(0)
    
    pos = 0      #Position to insert merged number
    left = i   #Initialize left partition position
    right = j + 1    #Initialize right partition position
    
    while left <= j and right <= k:
        if values[left] < values[right]:
            sorted_list[pos] = values[left]
            left += 1
        else:
            sorted_list[pos] = values[right]
            right += 1
        pos += 1
    
    while left <= j:
        sorted_list[pos] = values[left]
        left += 1
        pos += 1
        
    while right <= k:
        sorted_list[pos] = values[right]
        right += 1
        pos += 1
    pos = 0
    
    while pos < merged_size:
        values[i + pos] = sorted_list[pos]
        pos += 1
    print(sorted_list)
    
    
    

def merge_sort(numbers, i, j):
    mid = 0
    if i < j:
        mid = (i + j) // 2
        merge_sort(numbers, i, mid)
        merge_sort(numbers, mid + 1, j)
        merge(numbers, i, mid, j)
        
array_numbers = [9, 0, 11, 10, 5, 8, 6, 7]
print("Merge Input:", array_numbers)
merge_sort(array_numbers, 0, len(array_numbers) - 1)
print("Result after Merge Sort:", array_numbers)