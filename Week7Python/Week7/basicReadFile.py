def main1():
    sportList = open("sports.txt")
    sp = sportList.read()
    print(sp)

def main2():
    sportList = open("sports.txt")
    sp = sportList.readline()
    print(sp)

def main3():
    sportList = open("sports.txt")
    for index in range(1, 11):
        sp = sportList.readline()
    print(str(index) + '. ', sp.rstrip())

def main4():
    sportList = open("sports.txt")
    for index in range(1, 11):
        sp = sportList.readline()
        if len(sp) >= 8:
            print(sp.rstrip())
    
main1()
main2()
main3()
main4()