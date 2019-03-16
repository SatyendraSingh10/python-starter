class Car(object):
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color


car2 = Car("Honda", "Accord", "blue")
print(car2.make + car2.model + car2.color)

car3 = Car("Accord", "Honda", "blue")
print(car3.make + car3.model + car3.color)
