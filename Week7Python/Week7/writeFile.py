def main():
    name = ""
    studentID = ""
    creditHours = ""
    fileName = "studentInfo.txt"
    inFile = open(fileName, "a") # a: append, w: override
    print("Information of 3 students.")
    for x in range(1, 4):
        print("\nEnter the information of student: " + str(x))
        name = input("Enter the name: ")
        studentID = input("Enter ID: ")
        creditHours = input("Enter the number of credits earned: ")
        
        inFile.write("Information of student: " + str(x))
        inFile.write("\nName: " + name)
        inFile.write("\nStudent ID: " + studentID)
        inFile.write("\nNumber of credits earned: " + creditHours)
        inFile.write("\n\n")
    inFile.close()
    print("Done! Data is saved in file: %s" %fileName)


main()