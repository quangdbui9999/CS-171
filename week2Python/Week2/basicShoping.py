itemName = input("Enter the name of the item: " )
numItems = int(input ("Enter the number of items: " ))
itemCost = float(input ("Enter the cost of one item: " ))

#Calculating Prie => Processing and storage

totalCost = numItems * itemCost

#Print results => Output
print("Item name: " , itemName )
print("Cost of one item: " , itemCost )
print("Number of items purchased: " , numItems )
print("Total Cost: $" , format (totalCost , "0.2f"), sep='')
# sep='': Any nested characters inside the '' characters of "sep = ''", the sep function will help separate to any character, integer or string, sep will be found in python 3.x or later.