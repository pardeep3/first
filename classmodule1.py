#quest 1

class Circle():
    def __init__(self,radius):
        self.r=radius
    def getarea(self):
        a=3.14*(self.r)
        print(a)
    def getcircumference(self):
        b=2*3.14*(self.r)
        print(b)
c=Circle(1)
c.getarea()
c.getcircumference()

#quest 2

class Student():
    def __init__(self,name,rollnumber):
        self.n=name
        self.r=rollnumber
    def display(self):
        print(self.n)
        print(self.r)
c=Student('varchla',143)
c.display()

#ques 3

class Temperature():
    def __init__(self,cel,far):
        self.c=cel
        self.f=far
    def convertcelsius(self):
         celsius=((self.f)-32)*(5/9)
         print(celsius)
    def convertfarenhiet(self):
         farenhiet=9/5*(self.c+32)
         print(farenhiet)
p=Temperature(0,68)
p.convertfarenhiet()
p.convertcelsius()

#quest 4

class Moviedetails():
    def __init__(self,moviename,artistname,yearofrealease,rating):
        self.m=moviename
        self.a=artistname
        self.y=yearofrealease
        self.r=rating
    def display(self):
        print(self.m)
        print(self.a)
        print(self.y)
        print(self.r)

    def update(self, moviename ,artistname ,yearofrealease,rating):
        self.q=moviename
        self.w=artistname
        self.e=yearofrealease
        self.t=rating
        print(self.q)
        print(self.w)
        print(self.e)
        print(self.t)
z=Moviedetails("race3","salman",2018,3)
z.display()
z.update("RACE","SAIF ALI KHAN",2008,4)

#ques 5

class Expenditure():
    expenditure = 50000
    savings = 1
    gpf=4500
    def __init__(self):
        print(self.expenditure)
        print(self.savings)
    def display(self):
        print(self.expenditure)
        print(self.savings)
        salary=500001
        totalsalary=(self.expenditure)+(self.savings)+(self.gpf)
        print(salary)
        print(totalsalary)
z=Expenditure()