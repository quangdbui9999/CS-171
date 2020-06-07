class Store:
    def __init__(self, hamburgers, fries, drinks):
        self.hamburgers = hamburgers
        self.fries = fries
        self.drinks = drinks
    
    def process(self):
        self.hamburgers = float(self.hamburgers) * 2.0
        self.fries = float(self.fries) * 1.5
        self.drinks = float(self.drinks) * 1.0
    
    def output_information(self):
        print(f"Hamburgers\' cost: {self.hamburgers}")
        print(f"Fries\' cost: {self.fries}")
        print(f"Drinkss\' cost: {self.drinks}")
    
cuahang = Store(input("Enter the number of Hamburgers: "), input("Enter the number of Fries: "), input("Enter the number of Drinks: "))
cuahang.process()
cuahang.output_information()