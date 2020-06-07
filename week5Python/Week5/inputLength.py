user_text = input()

''' Type your code here. '''
counter = 0
for index in range(len(user_text)):
    if(65 <= ord(user_text[index]) <= 90 or 97 <= ord(user_text[index]) <= 122 or ord(user_text[index]) == 33):
        counter += 1
print(counter)