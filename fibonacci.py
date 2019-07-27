n1=0
n2=1
num=int(input("Number:"))
print(n1,n2,end=" ")
while(num-2):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
    num=num-1
