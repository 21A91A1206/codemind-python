n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
mi=999
c=0
for i in l:
    if(i>=a)and(i<=b):
        if i<mi:
            mi=i
            c+=1
if c==0:
    print("-1")
else:
    print(mi)