#ques 1

class Animal():
    def Animal_attribute(self):
        print("lion")
class Tiger(Animal):
    print("dog")
a=Tiger()
a.Animal_attribute()

#ques 2

print("output = (A,B),(A,B)")

#ques 3

class Cop():
    def __init__(self,name,age,work,experience,designation):
        self.n= name
        self.a= age
        self.w= work
        self.e= experience
        self.d= designation
    def add(self):
        print("following details of the cop is")
    def display(self):
        print("name is : "  + self.n)
        print("age  is : " + self.a)
        print("work  is : " + self.w)
        print("experience is  : " + self.e)
        print("designation  is : " + self.d)
    def Update(self,name,age,work,experience,designation):
       self.z= name
       self.x= age
       self.c= work
       self.v= experience
       self.b= designation
       print("name is  : "  + self.z)
       print("age  is  : " + self.x)
       print("work  is : " + self.c)
       print("experience  is  : " + self.v)
       print("designation  is : " + self.b)
class Mission(Cop):
    print("mission details of cop")
m=Mission("varchla thakur",str(25),"work for air force","no experience","air force")
m.add()
m.display()
m.Update("varchla thakur",str(21),"work for army","completed 5 missions","army")

#ques 4

class Shape():
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
class Rectangle(Shape):
    def Area1(self):
        rectangle=self.l*self.b
        print(rectangle)
class Square(Rectangle):
    def Area2(self):
        square=self.l*4
        print(square)
m=Square(2,2)
m.Area1()
m.Area2()
