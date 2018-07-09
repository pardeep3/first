#ques 1

try:
    a=3
    if(a<4):
        a=a/(a-3)
        raise handle
except ZeroDivisionError:
    print("zero division error")
#it is zero division error

#ques 2

try:
    import deepali
    l=[1,2,3]
    print(l[3])
except Exception:
    print("index error")
#it is index error

#ques 3

try:
    raise NameError("hi there")
except NameError:
    print("An exception")

#ques 4

def abyB(a ,b):
    try:
        c =((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
#driver program to test above function

abyB(2.0 ,3.0)
abyB(3.0 ,3.0)

#ques 5

#import error
try:
    import deepali
except ImportError:
    print("enter a import file")
#value error
try:
    a = int(input("enter no"))
except ValueError:
    print("please enter Int")

#ques 6

class Ageerror(Exception):
    pass
a=True
while(a):
    try:
        age=int(input("enter age"))
        if(age>=18):
            a=False
            raise Ageerror
        else:
            print(age)
    except Ageerror:
        print("age is greater than 18")
    except ValueError:
        print("only int allowed")
