print(3 + 2 * 2)

name = 'Lizz'
print(name[0:2])

var = '01234567'

print(var[::2])

print('1' + '2')

A = (0, 1, 2, 3)
print(A[-1])
print(A[3])

B = ["a", "b", "c"]
print(B[1:])

D = {'a': 0, 'b': 1, 'c': 2}
print(D.values())

L = ['c', 'd']
L.append(['a', 'b'])
print(L)
print(len(L))

print(bool(1))

Numbers = "0123456"
print(Numbers[::2])

print("0123456".find('1'))

i = 100000000
print(i != 0)

Dict = {"A": 1, "B": "2", "C": [3, 3, 3], "D": (4, 4, 4), 'E': 5, 'F': 6}

x = 'a'

if x != 'a':
    print("this is not a")

else:
    print("this is a")

release_year = 1993
if (release_year < 1980) or (release_year == 1991) or (release_year == 1993):
    print(release_year)

A = [3, 4, 5]
for a in A:
    print(a)

x = 3
y = 1
while y != x:
    print(y)
    y = y + 1

for i in range(-5, 5):
    print(i)

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while squares[i] == 'orange':
    new_squares.append(squares[i])
    i += 1

print(new_squares)

x = 1

if x != 1:

    print('Hello')

else:

    print('Hi')

print('Mike')

A = ['1', '2', '3']
for a in A:
    print(2 * a)
