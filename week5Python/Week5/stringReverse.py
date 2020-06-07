''' Type your code here. '''

def reverse_string(string_name):
    return string_name[len(string_name)::-1]


prompt = input()
while prompt.lower() != "quit" and prompt.lower() != 'q':
    print(reverse_string(prompt))
    enter_string = input()
    prompt = enter_string