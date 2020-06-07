# Type all other functions here

def print_menu(usr_str):
    menu_op = ' '
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit\n")

    menu_op = input("Choose an option:\n")
    # check valid or invalid character
    while (
            menu_op == 'c' and menu_op == 'w' and menu_op == 's' and menu_op == 'r' and menu_op == 'f' and menu_op == 'q'):
        menu_op = input("Choose an option:\n")
    # Complete print_menu() function
    return menu_op, usr_str


def get_num_of_non_WS_characters(what_string):
    num_character = 0
    for i in what_string:
        if (i != "\n" and i != " " and i != "\t"):
            num_character += 1
    return num_character


def get_num_of_words(what_string):
    number_words = what_string.split()
    return len(number_words)


def convertStringToList(what_string):
    what_list = []
    for what_character in what_string:
        what_list.append(what_character)
    return what_list


def convertCharListtoString(what_list):
    new_string = ""
    for what_character in what_list:
        new_string += what_character
    return new_string


def fix_capitalization(what_string):
    number_capitalization = 0
    updated_string = " "
    capitalization_after = ('.', '!', '?', ':')
    flag_capitalization = True
    list_character = convertStringToList(what_string)

    for index, what_char in enumerate(list_character):
        # get the first character after the symbols in tuple capitalization_after
        if (flag_capitalization == True and what_char != ' '):
            list_character[index] = what_string[index].upper()
            number_capitalization += 1
            flag_capitalization = False
        if (what_char in capitalization_after):
            flag_capitalization = True
    updated_string = convertCharListtoString(list_character)

    return (updated_string, number_capitalization)


def replace_punctuation(what_string, exclamation_count=0, semicolon_count=0):
    updated_string = ""
    list_character = []
    new_list_character = []

    for character in what_string:
        list_character.append(character)

    for index in list_character:
        if index == '!':
            exclamation_count += 1
            index = '.'
            new_list_character.append(index)
        elif index == ';':
            semicolon_count += 1
            index = ','
            new_list_character.append(index)
        else:
            new_list_character.append(index)

    for index in new_list_character:
        updated_string += index
    print("Punctuation replaced")
    print(f"exclamation_count: {exclamation_count}")
    print(f"semicolon_count: {semicolon_count}")
    return updated_string

def shorten_space(what_string):
    remove_space = what_string.split()
    connect_string = " ".join(remove_space)
    return connect_string


if __name__ == '__main__':
    # Complete main section of code
    sample_text = input("Enter a sample text:\n")
    print(f"\nYou entered: {sample_text}\n")

    option_menu = ""
    while (option_menu != "q"):
        option_menu, user_input = print_menu(sample_text)

        if (option_menu == "c"):
            num_non_whitespace = get_num_of_non_WS_characters(user_input)
            print(f"Number of non-whitespace characters: {num_non_whitespace}\n")
        elif (option_menu == "w"):
            num_words = get_num_of_words(user_input)
            print(f"Number of words: {num_words}\n")
        elif (option_menu == "f"):
            new_string, number_capitalization = fix_capitalization(user_input)
            print(f"Number of letters capitalized: {number_capitalization}")
            print(f"Edited text: {new_string}\n")
        elif (option_menu == "r"):
            new_string = replace_punctuation(user_input)
            print(f'Edited text: {new_string}\n')
        elif (option_menu == "s"):
            cut_redundant_space = shorten_space(user_input)
            print(f"Edited text: {cut_redundant_space}\n")