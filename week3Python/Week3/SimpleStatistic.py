num1 = float(input())
num2 = float(input())
num3 = float(input())

''' Type your code here. '''
average = (num1 + num2 + num3) / 3
average_int = int(average)
product = num1 * num2 * num3
product_int = int(product)
print(str(average_int) + " " + str(product_int))
print("%.2f %.2f" % (average, product))