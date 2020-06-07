def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print("Welcome to Fraction Simplifier")
print('Type "exit" to quit.')
str_fraction = input("Enter Fraction (Int/Int):\n")
exit = False

while str_fraction != 'exit':
    list_int = str_fraction.split('/')
    nominator = int(list_int[0])
    denominator = int(list_int[1])
    
    simple = gcd(nominator, denominator)
    nominator = int(nominator / simple)
    denominator = int(denominator / simple)
    
    print('Simplified Fraction')
    if(nominator % denominator == 0):
        print(f"{nominator}")
    else:
        print(f"{nominator}/{denominator}")
    str_fraction = input("Enter Fraction (Int/Int):\n")
print("Bye.")