#Functions and recursion
def area_of_circle(r):
    print("Area of a circle",2*3.14*r)
area_of_circle(5)

#default parameter
def students(name="Anish"):
    print("This student is from Aml department",name)
students("Abishek J")
students("Ajay")
students("Adhithya")
students()

#lambda expressions
y= lambda a,b,c,d:a*b*c*d
print(y(10,43,24,78))

# class and objects
class house:
    floor=2
    rooms=4
    entrance=2
flr=house()
print(flr.floor)
rms=house()
print(rms.rooms)
erance=house()
print(erance.entrance)


class triangle:
    half=0.5
    base=0
    height=0
def calculate_area():
    print("Area of a triangle",half*base*height)
tri=triangle()
x=tri.base(42)
y=tri.height(35)
calculate_area()


#Class and objects
class animal:
    def omnivorous(self):
        print("This animal belongs to omnivorous species")
class dog(animal):
    def __init__(self,bark,breed):
        print("This is a dog")
        self.bark=bark
        self.breed=breed
    def barks(self):
     print("Dog will bark")
class cat(animal):
    print("This is a cat")
    def __init__(self,meow,breed):
        self.meow=meow
        self.breed=breed
    def moos(self):
        print("Cat meows")
D=dog("bark","golden retriever")
D.barks()
D.omnivorous()
c=cat("meow","burmese")
c.moos()
c.omnivorous()

#class and objects for aml department
class college:
    def general_purpose(self):
        print("It provides knowledge to students")
class Department(college):
    def __init__(self,name,code):
        print("You belong to aml department")
        self.name=name
        self.code=code
    def specific_Department(self):
        print("This department provides knowledge about artificial intelligence and machine learning")
c=Department("Aml",3123)
c.general_purpose()
c.specific_Department()

#Iterators
class channels:
    def __init__(self):
        self.channels=["Ngo","Espn","Ssn","Bbc"]
        self.index=-1
    def __iter__(self):
        self.index=1
        
