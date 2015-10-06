n=int(input())
a=input().split()
f=True
i=0
while f:
    if a[i+1:].count(a[i])>0:
        f=False
        print(a[i])
    i+=1

