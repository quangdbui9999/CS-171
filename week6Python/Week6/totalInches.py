def print_total_inches(num_feet, num_inches):
    total_height = num_feet * 12 + num_inches
    print("Total inches: %d" %total_height)

feet = int(input())
inches = int(input())
print_total_inches(feet, inches)