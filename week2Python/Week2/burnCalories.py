''' Men: Calories = ((Age x 0.2017) - (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''
''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''

''' Type your code here. '''
class BurnCalories:
    def __init__(self, age, weight, heart_rate, time):
        self.age = age
        self.weight = weight
        self.heart_rate = heart_rate
        self.time = time
    
    def process_information(self, men_calories = 0, women_calories = 0):
        men_calories = ((self.age * 0.2017) - (self.weight * 0.09036) + (self.heart_rate * 0.6309) - 55.0969) * self.time / 4.184
        women_calories = ((self.age * 0.074) - (self.weight * 0.05741) + (self.heart_rate * 0.4472) - 20.4022) * self.time / 4.184
        return 'Men: {:.2f} calories\nWomen: {:.2f} calories'.format(men_calories, women_calories)

who = BurnCalories(age = int(input()),
        weight = float(input()),
        heart_rate = float(input()),
        time = int(input()))
print(who.process_information())
