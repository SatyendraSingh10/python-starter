class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print('My name : ' + self.name)
        print('My age : ' + str(self.age))


# set name and age to classes object
p1 = Person('satyendra', 30)
print(p1.name)
print(p1.age)

# us classes function
print(p1.info())
