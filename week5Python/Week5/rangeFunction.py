for x in range(5):
    print(x, end=" ")
print() #0 1 2 3 4

for x in range(1,5):
    print(x, end=" ")
print() # 1 2 3 4

for x in range(3,20,2):
    print(x, end=" ")
print() # 3 5 7 9 11 13 15 17 19 

numIteration = 6
for x in range(numIteration):
    print(x, end=" ")
print() # 0 1 2 3 4 5 

numIteration = 6
for x in range(numIteration + 1):
    print(x, end=" ")
print() # 0 1 2 3 4 5 6

for x in [3,6,9,12,15,18]:
    print(x, end = " ")
print()
for x in range(3, 19, 3):
    print(x, end = " ")
print()

for x in range(100, 201, 2):
    print(x)
'''
100
102
104
106
108
110
112
114
116
118
120
122
124
126
128
130
132
134
136
138
140
142
144
146
148
150
152
154
156
158
160
162
164
166
168
170
172
174
176
178
180
182
184
186
188
190
192
194
196
198
200
'''
for x in range(5, -1, -1):
    print(x)
'''
5
4
3
2
1
0
'''
for odd_number in range(1, 100, 2):
    print(odd_number)
for x in range(5, 501, 5):
    print(x, end = " ")