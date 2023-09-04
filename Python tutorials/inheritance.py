class vehicle: #parent class
    def general_usage(self):
        print("general use: transportation")

class car(vehicle): #derived class1
    def __init__(self):
        print("I'm a car")
        self.wheels = 4
        self.has_roof = True
    def specific_usage(self):
        print("specific use: commute to work")
class motorcycle(vehicle): #derived class2
    def __init__(self):
        print("I'm a motorcycle")
        self.wheels = 2
        self.has_roof = False
    def specific_usage(self):
        print("specific use: racing")

c = car() #object1
c.general_usage()
c.specific_usage()

m = motorcycle() #object2
m.general_usage()
m.specific_usage()
