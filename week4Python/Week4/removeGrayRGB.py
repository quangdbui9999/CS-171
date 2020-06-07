''' Type your code here. '''
red = int(input())
green = int(input())
blue = int(input())

red_color = 0
green_color = 0
blue_color = 0
gray = 50

if((0 <= red <= 255) and (0 <= blue <= 255) and (0 <= green <= 255)):
    if(50 <= red < 255):
        red_color = red - gray
    else:
        red_color = red
    if(50 <= green < 255):
        green_color = green - gray
    else:
        green_color = green
    if(50 <= blue < 255):
        blue_color = blue - gray
    else:
        blue_color = blue
    if (red == 0) and (green == 0) and (blue == 0):
        red_color = 0
        green_color = 0
        blue_color = 0
    elif (red == 255) and (green == 255) and (blue == 255):
        red_color = 0
        green_color = 0
        blue_color = 0
    if(red < green < blue) and (red != 0):
        red_color = red - red
        green_color = green - red
        blue_color = blue - red
    print(f"{red_color} {green_color} {blue_color}")