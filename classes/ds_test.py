import numpy as np

print(3 + 2 * 2)

print(type(True))
print(int(3.2))

A = '1234567'
print(A[1::2])

Name = "Michael Jackson"
print(Name.find('el'))

print('1,2,3,4'.split(','))

for n in range(3):
    print(n)


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p1 = Points(1, 2)

p1.print_point()
