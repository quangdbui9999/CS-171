def hanoi(start, spare, end, n):
    if n == 1:
        print(start + " -> " + end)
    else:
        hanoi(start, end, spare, n - 1)
        print(start + " -> " + end)
        hanoi(spare, start, end, n - 1)

hanoi("A", "B", "C", 4)