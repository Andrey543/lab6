input=open('input.txt','r')
output=open('output.txt','w')
n=int(input.readline().rstrip())
f=True
i=0
a = list(map(int,input.readline().split()))
a.sort()
while f:
    if a[i]==a[i+1]:
        f=False
        print(a[i],file=output)
    i+=1


