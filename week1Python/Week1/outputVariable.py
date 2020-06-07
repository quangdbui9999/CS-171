user_num = int(input('Enter integer:\n'))

# Type your code here

def output_1(user_num):
    print(f"You entered: {user_num}")
    square_num = user_num * user_num
    cubed_num = square_num * user_num
    print(f"{user_num} squared is {square_num}")
    print(f"And {user_num} cubed is {cubed_num} !!")
    
    another_number = int(input("Enter another integer:\n"))
    sum = user_num + another_number
    product = user_num * another_number
    print(f"{user_num} + {another_number} is {sum}")
    print(f"{user_num} * {another_number} is {product}")


output_1(user_num)