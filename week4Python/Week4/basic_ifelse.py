'''

State the meaning of each of the following conditional operators. If you are not sure of the meaning of
any symbol, create some example expressions, type them into the Python interpreter and examine the
results.
(a) (1 point) <   less than
(b) (1 point) >   greater than
(c) (1 point) <=  less than or equal to
(d) (1 point) >=  greater than or equal to
(e) (1 point) !=  does not equal
(f) (1 point) ==  equal

-----------------------------------------------

x = 4
y = 5
z = 4
(a) (1 point) x > y    False
(b) (1 point) x < y    True
(c) (1 point) x == y   False
(d) (1 point) x != y   True
(e) (1 point) x >= z   True
(f) (1 point) x <= z   True
(g) (1 point) x + y > 2 * x     9 > 8 (True)
(h) (1 point) y * x - z != 4 % 4 + 16    :  16 != 16  (False)
(i) (1 point) pow(x,2) == abs(-16)  16==16 (True)


---------------------

Strings are compared character by character based on
the ASCII/Unicode values for each character
- Lexicographic order
- If the shorter word is substring of a longer word, the
longer word is greater than the shorter word
- String comparisons are case sensitive
- The lower() and upper() string methods can change the case of a string to upper or lower.

-------------------

if num1 == num2:
    print("num1 == num2")
else:
    print("num1 != num2")
    
'''

word1 = "hello"
word2 = "good -bye"
if word1 == word2:
    print('word1 == word2') #False
if word1 != word2:
    print('word1 != word2') #True
if word1 < word2:
    print('word1 < word2') # False
if word1 >= word2:
    print('word1 >= word2') # True