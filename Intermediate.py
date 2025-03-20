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
