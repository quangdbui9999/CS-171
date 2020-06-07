
def counterVowels(what_string):
    counter = 0
    vowels = ('a', 'e', 'i', 'o', 'y', 'u')
    for i in what_string:
        print(i)
        if i.lower() in vowels:
            counter += 1
    return counter

str = "Quang Bui"
print(f"Number of vowels are: {counterVowels(str)}")o