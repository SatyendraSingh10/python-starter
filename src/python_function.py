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

# call to hello python
hello_python_function()


def delta(x):
    if x == 0:
        y = 1
    else:
        y = 0
    return y


print(delta(0))
