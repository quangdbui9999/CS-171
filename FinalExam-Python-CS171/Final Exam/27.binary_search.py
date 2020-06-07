
def binary_search(values, start, end, key):
    if start > end:
        return -1
    mid = (start + end) // 2
    if(values[mid] == key):
        return mid
    elif values[mid] < key:
        return binary_search(values, mid + 1, end, key)
    else:
        return binary_search(values, start, mid - 1, key)

def binary_search_V2(values, key):
    start = 0
    end = len(values) - 1
    count = 0
    
    while end >= start:
        count += 1
        print(f"The function running {count} times.")
        mid = (end + start) // 2
        print(f"The mid value is: {values[mid]} at position {mid}")
        if(values[mid] < key):
            start = mid + 1
        elif values[mid] > key:
            end = mid - 1
        else:
            return mid
    return - 1
        
    
list_numbers = [12, 17, 22, 34, 48, 51, 55, 62]
count = 0
key = 48
#position_number = binary_search(list_numbers, 0, len(list_numbers), key)
position_number = binary_search_V2(list_numbers, key)
if(position_number == -1):
    print(f"The number {key} is not in the list.")
else:
    print(f"Number {key} at position {position_number} after {count} running.")
