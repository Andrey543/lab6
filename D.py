k=0
l=0
input=open('input.txt','r')
output=open('output.txt','w')
b=input.readline().split()
k=int(b[0])
n=int(b[1])
a=input.readline().split()
for i in range(k-1):
    a1=input.readline().split()
    for j in range(n):
        a[j]=min(a1[j],a[j])
print(' '.join(a), file=output)