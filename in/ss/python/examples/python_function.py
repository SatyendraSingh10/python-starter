def hello_python_function():
    print('Hello python from function')


def add1(a):
    b = a + 1
    return b


a = 1


def add(b):
    return a + b


c = add(10)
print(c)


def f(*x):
    return sum(c)


print(f(2, 3))
# call to hello python
hello_python_function()
