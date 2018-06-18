# ques 1
year=int(input("enter year"))
if((year%4)==0):
    print("it s a leap year")
else:
    print("it is not a leap year")

# ques 2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("it is  square")
else:
    print("it is a rectangle")

# ques 3
a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))
if((a>b) and (a>c)):
    print("a is oldest")
elif ((b>a) and (b> c)):
        print("b is oldest")
else:
    print("c is oldest")

a = int(input("enter age"))
b = int(input("enter age"))
c = int(input("enter age"))
if ((a <b) and (a < c)):
    print("a is younger")
elif ((b < a) and (b < c)):
    print("b is younger")
else:
    print("c is younger")

# ques 4
points=int(input("enter points"))
if((points>1) and (points<50)):
    print(" sorry no prize this time")
if((points>51) and (points<150)):
    print("congratulation you won wooden dog")
if((points>151) and (points<180)):
    print(" congratulation you won book")
if((points>181) and (points<200)):
    print("congratulation you won chocalate")
else:
    print("wrong input")

# ques 5
unit=int(input("enter units"))
cost=(unit*100)
print("total cost", cost)
if(cost>1000):
    print("cost after discount",cost*0.10)
else:
    print("cost",cost)
