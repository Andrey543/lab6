input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline().rstrip())
a=input.readline().rstrip() 
f=True
i=0
while f:
    if a.find(a[i],i+1)!=-1:
        f=False
        print(a[i],file=output)
    i+=2


