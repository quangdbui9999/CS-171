word = input('Enter a word: ')
if 'apple' <= word.lower() <= 'pear':
    print(f"{word} is valid")
else:
    print(f'{word} is out of range')