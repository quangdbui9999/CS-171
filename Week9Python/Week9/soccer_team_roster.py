# Type code here
def input_int(number, lower_bound, upper_bound):
    valid = False
    while not valid:
        try:
            x = input(number)
            x = int(x)
            if(x < lower_bound or x > upper_bound):
                valid = False
            else:
                return x
        except ValueError as e:
            valid = False

def print_menu():
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit\n")
    select = input("Choose an option:\n")
    return select

def output_information(key_sorted, my_diction, above_number = 0):
    if(above_number == 0):
        print("ROSTER")
        for index in key_sorted:
            print(f"Jersey number: {index}, Rating: {my_diction[index]}")
    else:
        print(f"ABOVE {above_number}")
        for index in key_sorted:
            if my_diction[index] > above_number:
                print(f"Jersey number: {index}, Rating: {my_diction[index]}")
    
if __name__ == '__main__':
    my_dictionary = {}
    
    for i in range(0, 5):
        jersey_number = input_int(f"Enter player {i + 1}'s jersey number:\n", 0, 99)
        rating = input_int(f"Enter player {i + 1}'s rating:\n\n", 0, 9)
        my_dictionary[jersey_number] = rating
        list_key = sorted(list(my_dictionary.keys()))
    
    output_information(list_key, my_dictionary)
    
    exit_program = False;
    
    while exit_program == False:
        user_input = print_menu()
        if(user_input == "a"):
            new_jersey_number = input_int(f"Enter a new player's jersey number:\n", 0, 99)
            new_rating = input_int(f"Enter the player's rating:\n", 0, 9)
            my_dictionary[new_jersey_number] = new_rating
            list_key = sorted(list(my_dictionary.keys()))
        elif(user_input == "d"):
            del_jersey_number = input_int(f"Enter a jersey number:\n", 0, 99)
            del my_dictionary[del_jersey_number]
            list_key = sorted(list(my_dictionary.keys()))
        elif(user_input == "u"):
            exist_jersey_number = input_int(f"Enter a jersey number:\n", 0, 99)
            new_rating = input_int(f"Enter a new rating for player:\n", 0, 9)
            my_dictionary[exist_jersey_number] = new_rating
            list_key = sorted(list(my_dictionary.keys()))
        elif(user_input == "r"):
            new_rating = input_int(f"Enter a rating:\n\n", 0, 9)
            output_information(list_key, my_dictionary, new_rating)
        elif(user_input == "o"):
            output_information(list_key, my_dictionary)
        elif(user_input == "q"):
            exit_program = True
    

'''
ROSTER
Jersey number: 4, Rating: 5
'''