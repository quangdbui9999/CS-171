def zone(age, rate):
    description = "";

    maximum_heart_rate = 220 - age
    training_heart_rate = maximum_heart_rate - rate

    if rate >= (0.9 * maximum_heart_rate):
        description = "Interval training"
    elif (0.7 * maximum_heart_rate) <= rate <= (0.9 * maximum_heart_rate):
        description = "Threshold training"
    elif (0.5 * maximum_heart_rate) <= rate <= (0.7 * maximum_heart_rate):
        description = "Aerobic training"
    elif rate < (0.5 * maximum_heart_rate):
        description = "Couch potato"

    return description


def input_int(number):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            return x
        except ValueError as e:
            valid = False


your_age = input_int("Enter your age: ")
your_rate = input_int("Enter your rate: ")
print("Answer: %s" % zone(your_age, your_rate))
