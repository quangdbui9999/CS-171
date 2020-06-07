print(16 + 3) # 19
print(16 - 3) # 13
print(16 * 3) # 48
print(16 ** 3)# 4096
print(16 / 3) # 5.33333333
print(16 // 3)# 5
print(16 % 3) # 1

age = 15
print("Your age is", age)
print("Your age is " + str(age))

answer = 6 ** 2 + 3 * 4 // 2 #42
final = answer % 4 #2
print(f"Answer: {answer}")
print(f"Final answer: {final}")

schoolName = "Drexel"
typeOfSchool = "University"
fullName = schoolName + typeOfSchool #DrexelUniversity
fullName = schoolName + " " + typeOfSchool
print(fullName)

addressNumber = 9701
streetName = "Germantown Ave"
streetAddress = str(addressNumber) + " " + streetName
print(streetAddress)

myWord = "Hello!" * 10
print (myWord)

fisrtNumber = int(input("Enter a number: "))
secondNumber = int(input("Enter another number: "))
difference = fisrtNumber - secondNumber
print("Difference =", difference)