user_input = input()
test_grades = list(map(int, user_input.split())) # contains test scores

sum_extra = -999 # Initialize 0 before your loop

''' Your solution goes here '''
sum_extra = 0
for index in test_grades:
    if index >= 100:
        sum_extra = sum_extra + (index - 100)
        
print('Sum extra:', sum_extra)