def hanoi1CallingSimplerMethods(start, end):
    print(start + " -> " + end)

def hanoi2CallingSimplerMethods(start, spare, end):
    hanoi1CallingSimplerMethods(start, spare)
    print(start + " -> " + end)
    hanoi1CallingSimplerMethods(spare, end)

def hanoi3CallingSimplerMethods(start, spare, end):
    hanoi2CallingSimplerMethods(start, end, spare)
    print(start + " -> " + end)
    hanoi2CallingSimplerMethods(spare, start, end)

def hanoi4CallingSimplerMethods(start, spare, end):
    hanoi3CallingSimplerMethods(start, end, spare)
    print(start + " -> " + end)
    hanoi3CallingSimplerMethods(spare, start, end)

hanoi4CallingSimplerMethods("A", "B", "C")