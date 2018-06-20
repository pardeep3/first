#ques 1

for i in range(1,10):
    print(input("enter value"))
    print(i)

#ques 2

x="True"
while(x=="rue"):
    print("loop is infinite")

#ques 3

l=[]
a=int(input("enter input"))
b=int(input("enter input"))
l.append(a)
l.append(b)
for i in l:
    print(i**2)

#ques 4

list = ["kirti" ,60 ,"deepsi" ,"gauri" ,29.2 ,23.45,89 ,"varchla"]
Int =[]
String =[]
Float =[]
for i in list:
    if isinstance(i,int):
        Int.append(i)

    elif  isinstance(i,str):
        String.append(i)

    else:
        Float.append(i)

print(Float)
print(Int)
print(String)
print("Float list =" +str(Float))
print("Int list = " +str(Int))
print("String list = " + str(String))

#ques 5

'''even=[]
odd=[]
for i in range(0,101):
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print("even number",even)
print("odd number",odd)
#ques 6
for i in  range(0,4):
    for i in range(0,i+1):
        print("*",end="")
    print()
#ques 7
dictionary={"name":"varchla","age":"19"}
for i in dictionary:
    dictionary.get(i)
    print(i)
#ques 8
l=[]
for i in range(0,5):
    num=int(input("enter the number:"))
    l.append(num)
print(l)
l2=[]
a=int(input("enter the value:"))
x=l.index(a)
x =l.remove(a)
print(l)'''
