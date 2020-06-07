class InputPractice:
    def __init__(self, user_int, user_float, user_char, user_string):
        self.user_int = user_int
        self.user_float = user_float
        self.user_char = user_char
        self.user_string = user_string
    
    def output(self):
        print(str(self.user_int) + " %.2f " %self.user_float + self.user_char + " " + self.user_string)
        print(self.user_string + " " + self.user_char + " %.2f " %self.user_float + str(self.user_int))
        print(str(self.user_int) + " converted to a character is " + chr(self.user_int))
        

who = InputPractice(int(input('Enter integer (32 - 126):\n')), float(input("Enter float:\n")), input("Enter character:\n"), input("Enter string:\n"))
who.output()