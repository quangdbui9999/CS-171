import random

def orderList(newList):
    newList.sort()
    newList.reverse()
    return newList

myList = []
for y in range(0, 100):
    myList.append(random.randint(1, 100))
print(orderList(myList))