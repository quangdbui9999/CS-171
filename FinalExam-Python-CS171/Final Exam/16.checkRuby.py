
list_string = ['Welcome Ruby', 'Ruby Programming', 'Check Ruby Program', 'nothing', 'Python & Ruby']
key = 'Ruby'
for i in list_string:
    if key in i:
        print("Hello Ruby: %s" %i)
    else:
        print("No Ruby: %s" %i)