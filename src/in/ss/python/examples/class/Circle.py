import matplotlib.pyplot as plt
% matplotlib
inline


class Circle(object):
    # this is constructor function
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def add_radius(self, r):
        self.radius = self.radius + r
        return self.radius

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()
