#ques 1

f=open("text.txt","r")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines"))
for i in range(0,n):
    print(a[i])
f.close()

#ques 2

a="kill"
f=open("text.txt","r")
k=f.read()
m=k.split()
print(k.count(a))

#ques 3

f=open("text.txt","r")
a=(f.readlines())
c=open("text2.txt","w")
c.writelines(a)

#ques 4

i=0
f=open("text.txt","r")
a=(f.read())
