import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 75,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input("Enter wall width (feet):\n"))
wall_area = wall_height * wall_width
print(f'Wall area: {wall_area} square feet')
paint_need = wall_area * float(1 / 350)
print('Paint needed: %0.2f gallons' %paint_need)
can_need = math.ceil(paint_need)
print("Cans needed: %d can(s)\n" %can_need)

select_color = input("Choose a color to paint the wall:\n")
print(f"Cost of purchasing {select_color} paint: ${paint_colors[select_color]}")
   
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall

# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer

# FIXME (4): Calculate and output the total cost of paint can needed depending on color
