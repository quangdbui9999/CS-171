hamburgers = float(input("Enter the number of Hamburgers: "))
fries = float(input("Enter the number of Fries: "))
drinks = float(input("Enter the number of Drinks: "))

#Processing data
hamburgersCost = hamburgers * 2.0
friesCost = fries * 1.5
drinksCost = drinks * 1.0
totalCost = hamburgersCost + friesCost + drinksCost

#Output data
print("Row  |  Value ")
print(f"Hamburgers\' cost: {hamburgersCost}")
print(f"Fries\' cost: {friesCost}")
print(f"Drinkss\' cost: {drinksCost}")
print("%18s | %6.2f" % ( "Hamburgers\' Cost" , hamburgersCost ))
print("%18s | %6.2f" % ( "Fries\' Cost" , friesCost ))
print("%18s | %6.2f" % ( "Drinks\' Cost" , drinksCost ))
print("%18s | %6.2f" % ( "Total Cost" , totalCost ))