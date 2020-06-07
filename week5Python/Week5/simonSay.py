user_score = 0
simon_pattern = input()
user_pattern  = input()

''' Your solution goes here '''
for index in range(len(simon_pattern)):
    if(user_pattern[index] == simon_pattern[index]):
        user_score += 1
    else:
        break
print('User score:', user_score)