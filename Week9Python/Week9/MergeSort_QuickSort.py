
'''
1)
a)
17, 12, 10, 15, 0, 14, 13, 5, 0, 6
0, 0, 5, 6, 10, 12, 13, 14, 15, 17

b)
11, 0, 10, 12, 3, 17, 11, 15, 7, 8
0, 3, 7, 8, 10, 11, 11, 12, 15, 17

c)
10, 19, 17, 0, 16, 3, 20, 14, 9, 1
0, 1, 3, 9, 10, 14, 16, 17, 19, 20

d)
7, 16, 20, 0, 20, 10, 11, 18, 0, 1
0, 0, 1, 7, 10, 11, 16, 18, 20, 20

e) We take the smallest number in the list and put this number in the
position 0, and then we take the second smallest number in the list and
put it in position 1, and so on. Finally, the largest number in the final
position. We have a sorted list from the smallest number to the
largest number.
A = [1, 3, 5]
B = [2, 6, 9]

2)
a) It is possible for both the following while statement to run if the list
has 2 or more numbers and it is possible for at most one run during the
specifical the function if the list have only one number.
Explain: The first step of Merge Sort is dividiving the list into both
list. If there is only one number, list B will receive that number,
list A is empty, that's why only list B run
c) When we encounter the element the same both lists, list B is the element
removed from first because if A[0] < B[0] (remove A), else (A[0] >= B[0],
removed B)

3)
a) If the length of a list is odd, the extra element go on the right

4)
Calling msort ([9,5,7,2])
Calling msort ([9,5])
Calling msort ([9])
Calling msort ([5])
Merge ([9]) and ([5]): ([5,9])
Calling msort ([7,2])
Calling msort ([7])
Calling msort ([2])
Merge ([7]) and ([2]): ([2,7])
Merge ([5,9]) and ([2,7]): ([2,5,7,9])

5)
(a) Partition the list: [68, 19, 86, 8, 64, 79, 77, 78, 18, 23] on the pivot value 23
Smaller Values: 19, 8, 18
Larger Values: 68, 86, 64, 79, 77, 78
(b) Parition the list [74, 62, 99, 63, 52, 74, 27, 78, 32, 6] on the pivot value 6
Smaller Values:
Larger Values: 74, 62, 99, 63, 52, 74, 27, 78, 32
(c) Parition the list [91, 8, 21, 86, 25, 73, 60, 49, 13, 46] on the pivot value 46
Smaller Values: 8, 21, 25, 13
Larger Values: 91, 86, 73, 60, 49
(d) Parition the list [53, 36, 60, 23, 51, 39, 68, 71, 92, 41] on the pivot value 41
Smaller Values: 36, 23, 39
Larger Values: 53, 60, 51, 68, 71, 92
(e) Parition the list [39, 9, 76, 30, 64, 26, 77, 13, 58, 38] on the pivot value 38
Smaller Values: Pivot: 9, 30, 26, 13
Larger Values: 39, 76, 64, 77, 58
          
          
6)
a) The function returns the value. They return the number of pivot position
QSORT(A, start, stop) function
b) Because p is the pivot number, pivot number will divide the list in two half,
low partition (any number less than p), and high partition (any number greater
than p). Values equal to the pivot may appear in either or both the partitions.
c) When start < stop, inside that condition we call the partition function .
This function will divide the list in 2 half, and we call 2 recursive quicksort
functions() to sort the number in left and right of the pivot until there
are no unsorted element
7)
a) Pivot number: stop value, the last element in the list
b)
def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp
swap(A, i, j)
'''


import random

def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp

def partition(A, start, stop):
    pivot = A[stop]
    i = start
    for j in range(start, stop):
        if(A[j] <= pivot):
            swap(A, i, j)
            i += 1
    swap(A, i, stop)
    return i

def qsort(A, start, stop):
    if start < stop:
        p = partition(A, start, stop)
        qsort(A, start, p - 1)
        qsort(A, p + 1, stop)

def merge(A, B):
    C = []
    while (len(A) > 0) and (len(B) > 0):
        if A[0] < B[0]:
            C.append(A[0])
            A.remove(A[0])
        else:
            C.append(B[0])
            B.remove(B[0])
    
    if len(A) > 0:
        C.append(A[0])
        A.remove(A[0])
    if len(B) > 0:
        C.append(B[0])
        B.remove(B[0])
    return C

def msort(X):
    if len(X) > 1:
        middle = len(X) // 2
        A = msort(X[:middle])
        B = msort(X[middle:])
        C = merge(A, B)
        return C
    else:
        return X
    
print(f"Lanh dia cua Quick Sort: ")
for x in range(0, 10):
    L = [random.randint(0, 100) for k in range(0, 10)]
    print("Quick Sort Input:", L)
    qsort(L, 0, len(L) - 1)
    print("Result after Quick Sort:", L)
print(f"\n\n\nLanh dia cua Merge Sort")
for x in range(0, 10):
    L = [random.randint(0, 100) for k in range(0, 10)]
    print("Merge Input:", L)
    L = msort(L)
    print("Result after Merge Sort:", L)
