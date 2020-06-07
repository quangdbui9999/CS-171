class FoodReceipt:
    def __init__(self, item_name, item_cost, item_quantity, price = 0.0):
        self.item_name = item_name
        self.item_cost = item_cost
        self.item_quantity = item_quantity
        self.price = price
    
    def output(self, item_name2 = "", item_cost2 = 0.0, item_quantity2 = 0):
        print("\nRECEIPT")
        
        self.price = self.item_quantity * self.item_cost
        print("%d %s @ $%0.2f = $%0.2f" %(self.item_quantity, self.item_name, self.item_cost, self.price))
        if(item_name2 != "" and item_cost2 != 0.0 and item_quantity2 != 0):
            price2 = item_cost2 * item_quantity2
            print("%d %s @ $%0.2f = $%0.2f" %(item_quantity2, item_name2, item_cost2, price2))
            self.price = self.price + price2
        
        print("Total cost: $%0.2f\n" %self.price)
    
    def output3(self):
        price_percentage = self.price * 0.15
        print("15%% gratuity: $%0.2f" %price_percentage)
        totalWithTip = price_percentage + self.price
        print("Total with tip: $%.2f" %totalWithTip)



whoBuy = FoodReceipt(input("Enter food item name:\n"), float(input("Enter item price:\n")), int(input("Enter item quantity:\n")))
whoBuy.output()
item_name2 = input("\nEnter second food item name:\n")
item_cost2 = float(input("Enter item price:\n"))
item_quantity2 = int(input("Enter item quantity:\n"))
whoBuy.output(item_name2, item_cost2, item_quantity2)
whoBuy.output3()



# FIXME (1): Finish reading item price and quantity, then output a receipt
   
# FIXME (2): Read in a second food item name, price, and quantity, then output a second receipt
   
# FIXME (3): Add a gratuity and total with tip to the second receipt