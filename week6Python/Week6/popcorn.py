
''' Your solution goes here '''
def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print("Too small")
    elif bag_ounces > 10:
        print("Too large")
    else:
        result = 6 * bag_ounces
        print(f"{result} seconds")
    

user_ounces = int(input())
print_popcorn_time(user_ounces)