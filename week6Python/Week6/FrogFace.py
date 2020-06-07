def printFrogFace():
    print("  @..@")
    print(" (-----)")
    print("(  >--< )")
    print("^ ^ __ ^ ^")

def main():
    printFrogFace()
    for x in range(4):
        print("Frog", (x + 1))
        printFrogFace()

main()
