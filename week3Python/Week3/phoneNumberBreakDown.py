phone_number = int(input())

''' Type your code here. '''

section1 = str(phone_number // 10000000)
section2 = str(phone_number // 10000 % 1000)
section3 = str(phone_number % 10000)
#+ str(phone_number // 1000000 % 10)
#+ str(phone_number // 10000 % 10)

print(section1 + "-" + section2 + "-" + section3)