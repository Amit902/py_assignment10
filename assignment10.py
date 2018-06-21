#Q1 Create a class Animal as a base class and define method animal_attribute.
#  Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def show(self):
        print("Animal")

class Tiger(Animal):
    def display(self):
        print("Tiger")

t=Tiger()
t.show()
t.display()


#Q2 What will be the output of following code.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()

print (a.f(), b.f())
print (a.g(), b.g())
print("THe above codes gives Syntax error and if we correct it then it gives the answer below")
print("A B")
print("A B")

#Q.3- Create a class Cop.
# Initialize its name, age , work experience and designation.
# Define methods to add, display and update the following details.
# Create another class Mission which extends the class Cop.
# Define method add_mission _details.
# Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class cop:
    def __init__(self,name,age,work_experience,designation):
        self.name=name
        self.age=age
        self.work_experience=work_experience
        self.designation=designation

    def display(self):
        print("Name: ",self.name)
        print("age: ",self.age)
        print("work exxperience:",self.work_experience)
        print("designation: ",self.designation)

    def update(self):
        self.name=input("Enter the name to update: ")
        self.age=input("age  : ")
        self.work_experience=input("Enter the work experience: ")
        self.designation=input("Designtion: ")

class mission(cop):
    def add_mission_detail(self):
        self.mission=input("enter mission detail : ")
        print("assign to mission: ",self.mission)

a=input("enter name: ")
b=input("enter age: ")
c=input("enter work experience: ")
d=input("designation: ")
x=mission(a,b,c,d)
x.display()
x.update()
x.add_mission_detail()
x.display()




#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
# Create class rectangle and square which inherits shape and access the method Area.

class shape:
    def __init__ (self,length,bredth):
        self.length=length
        self.bredth=bredth

class rectangle(shape):
    def area(self):
        area=self.length*self.bredth
        print(area)

class square(shape):
    def area(self):
        area=self.length*self.bredth
        print(area)
x=rectangle(5,10)
x.area()
y=square(5,5)
y.area()