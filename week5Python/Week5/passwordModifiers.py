word = input()
password = ''

''' Type your code here. '''
end_string = "q*s"
for index in word:
    if index == 'i':
        password += index.replace('i', '!')
    elif index == 'a':
        password += index.replace('a', '@')
    elif index == 'm':
        password += index.replace('m', 'M')
    elif index == 'B':
        password += index.replace('B', '8')
    elif index == 'o':
        password += index.replace('o', '.')
    else:
        password += index
print(password + end_string)
'''
i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
'''