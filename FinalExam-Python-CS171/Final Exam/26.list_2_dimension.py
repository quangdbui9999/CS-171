
numbers = [
    [1, 2],
    [10, 20],
    [1000, 2000],
    [10000, 20000]
]

num_rows = 0
num_cols = 0
print("Contents of the List Number")
for row in numbers:
    num_rows += 1
    for cell in row:
        num_cols += 1
        print(cell, end = ' ')
    print()
print(f"Number of rows: {num_rows}.")
print(f"Number of columns: {int(num_cols / num_rows)}.")