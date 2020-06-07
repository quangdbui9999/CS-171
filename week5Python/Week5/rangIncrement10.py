''' Type your code here. '''
step = 10
start = int(input())
end = int(input())
if(end < start):
    print("Second integer can't be less than the first.", end="")
else:
    for x in range(start, end + 1, step):
        print(x, end = " ")
print()