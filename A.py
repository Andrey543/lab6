input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline().rstrip())
f=True
i=0
x=input.read(1)
a = list(map(int,input.readline().split()))
while f:
    if a[i+1:].count(a[i])>0:
        f=False
        print(a[i],file=output)
    i+=1


