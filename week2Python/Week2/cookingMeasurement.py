class CookingMeasurementConverter:
    def __init__(self, lemon_juice_cups, water_cups, sugar_cups, number_servings):
        self.lemon_juice_cups = lemon_juice_cups
        self.water_cups = water_cups
        self.sugar_cups = sugar_cups
        self.number_servings = number_servings
    
    def output(self, num_serving = 0):
        if num_serving == 0:
            print("\nLemonade ingredients - yields %0.2f servings" %self.number_servings)
        else:
            print("\nLemonade ingredients - yields %0.2f servings" %num_serving)
        print("%0.2f cup(s) lemon juice" %self.lemon_juice_cups)
        print("%0.2f cup(s) water" %self.water_cups)
        print("%0.2f cup(s) agave nectar" %self.sugar_cups)
    
    def process_information2(self, num_serving):
        serving = num_serving / self.number_servings
        self.lemon_juice_cups = self.lemon_juice_cups * serving
        self.water_cups = self.water_cups * serving
        self.sugar_cups = self.sugar_cups * serving
        
    def process_information3(self, num_serving):
        self.lemon_juice_cups = self.lemon_juice_cups / 16
        self.water_cups = self.water_cups / 16
        self.sugar_cups = self.sugar_cups / 16
    
    def output_information3(self, serving):
        print()
        print("Lemonade ingredients - yields %.2f servings" % serving)
        print("%0.2f gallon(s) lemon juice" %self.lemon_juice_cups)
        print("%0.2f gallon(s) water" %self.water_cups)
        print("%0.2f gallon(s) agave nectar" %self.sugar_cups)
        

ingredient = CookingMeasurementConverter(float(input('Enter amount of lemon juice (in cups):\n')), float(input("Enter amount of water (in cups):\n")), float(input("Enter amount of agave nectar (in cups):\n")), float(input("How many servings does this make?\n")))
ingredient.output()
print()
serving = float(input("How many servings would you like to make?\n"))
ingredient.process_information2(serving)
ingredient.output(serving)
ingredient.process_information3(serving)
ingredient.output_information3(serving)
