#ques 1

radius=float(input("enter no"))
def area(rad):
    return 3.14*rad*rad
ar=area(radius)
print(ar)

#ques 2

n=6
def perfect(n):
    sum = 0
    for i in range (1,n):
        if(n%i==0):
            sum=sum+i
    if (sum==n):
        return True
    else:
        return False


for i in range(1,1001):
    if(perfect(i)==True):
        print(i)


# ques 3

num=12
def table(num):
    for i in range(1, 11):
        print(str(num) + " * " + str(i) + "=", num * i)


print(table(num))


# ques 4
a=int(input("enter a"))
b=int(input("enter b"))
def power(a, b):
    if(b == 1):
        return a
    else:
        return(a * power(a, b - 1))


print(power(a,b))

# ques 5
n=1
def recur_factorial(n):
   if(n == 1):
       return n
   else:
       return n*recur_factorial(n-1)


num=int(input("enter no"))

if(num < 0):
   print("Sorry, factorial does not exist for negative numbers")
elif(num == 0):
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",recur_factorial(num))

