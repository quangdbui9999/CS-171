fileName = "1404.txt"
countDigit = 0
with open(fileName, "r") as lines:
    line = lines.readline()
    while line:
        for word in line.split():
            if(word.isdigit() == True):
                countDigit += 1
                print(word)
        line = lines.readline()
print(f"There are {countDigit} in file {fileName}.")