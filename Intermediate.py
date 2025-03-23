# Functions and recursion
def area_of_circle(r):
    print("Area of a circle:", 3.14 * r * r)  # Corrected formula for area

area_of_circle(5)

# Default parameter
def students(name="Anish"):
    print("This student is from AML department:", name)

students("Abishek J")
students("Ajay")
students("Adhithya")
students()

# Lambda expressions
y = lambda a, b, c, d: a * b * c * d
print(y(10, 43, 24, 78))

# Class and objects
class House:
    def __init__(self):
        self.floor = 2
        self.rooms = 4
        self.entrance = 2

flr = House()
print(flr.floor)
print(flr.rooms)
print(flr.entrance)

# Class and objects with methods
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

tri = Triangle(42, 35)
print("Area of a triangle:", tri.calculate_area())

# Class inheritance
class Animal:
    def omnivorous(self):
        print("This animal belongs to omnivorous species")

class Dog(Animal):
    def __init__(self, bark, breed):
        super().__init__()
        print("This is a dog")
        self.bark = bark
        self.breed = breed
    
    def barks(self):
        print("Dog will bark")

class Cat(Animal):
    def __init__(self, meow, breed):
        super().__init__()
        print("This is a cat")
        self.meow = meow
        self.breed = breed
    
    def meows(self):
        print("Cat meows")

D = Dog("bark", "Golden Retriever")
D.barks()
D.omnivorous()

C = Cat("meow", "Burmese")
C.meows()
C.omnivorous()

# Class and objects for AML department
class College:
    def general_purpose(self):
        print("It provides knowledge to students")

class Department(College):
    def __init__(self, name, code):
        super().__init__()
        print("You belong to AML department")
        self.name = name
        self.code = code
    
    def specific_department(self):
        print("This department provides knowledge about artificial intelligence and machine learning")

c = Department("AML", 3123)
c.general_purpose()
c.specific_department()

# Iterators
class Channels:
    def __init__(self):
        self.channels = ["Ngo", "Espn", "Ssn", "Bbc"]
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.channels):
            raise StopIteration
        channel = self.channels[self.index]
        self.index += 1
        return channel

ch = Channels()
for c in ch:
    print(c)

# Dept HOD, AML, Students
class Aml:
    def __init__(self, name, occupation, age=None):
        self.name = name
        self.occupation = occupation
        self.age = age
    
    def work(self):
        if self.occupation == "Head of department" and self.age == 50:  # Fixed comparison operator
            print(self.name, "is the head of the department")
        elif self.occupation == "Associate professor":
            print(self.name, "is the associate professor")
        else:
            print(self.name, "is the assistant professor")

aiml = Aml("Lilly Raamesh", "Head of department", 50)  # Fixed argument format
aiml.work()