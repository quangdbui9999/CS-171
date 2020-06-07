# FIXME (1): Finish reading another word and an integer into variables. 
# Output all the values on a single line
#favorite_color = input('Enter favorite color:\n')


# FIXME (2): Output two password options
#password1 = favorite_color
#print('\nFirst password:')


# FIXME (3): Output the length of the two password options
favorite_color = input("Enter favorite color:\n")
pet_name = input("Enter pet's name:\n")
number = int(input("Enter a number:\n"))
print(f"You entered: {favorite_color} {pet_name} {number}\n")

string_pass1 = f"{favorite_color}_{pet_name}";
string_pass2 = f"{number}{favorite_color}{number}";

print(f"First password: {string_pass1}")
print(f"Second password: {string_pass2}\n")

print(f"Number of characters in {favorite_color}_{pet_name}:", len(string_pass1))
print(f"Number of characters in {number}{favorite_color}{number}:", len(string_pass2))