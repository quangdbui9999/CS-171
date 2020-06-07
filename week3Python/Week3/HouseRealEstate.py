current_price = int(input())
last_months_price = int(input())

''' Type your code here. '''
change = current_price - last_months_price
estimate_monthly = (current_price * 0.045) / 12
print("This house is $%d. The change is $%d since last month." %(current_price, change))
print("The estimated monthly mortgage is $%0.2f." %estimate_monthly)