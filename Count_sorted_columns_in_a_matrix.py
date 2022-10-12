m,n=map(int,input().split())
l=[]
s=0
for p in range(n):
    l.append([])
for i in range(m):
    a=list(map(int,input().split()))
    for j in range(n):
        l[j].append(a[j])
for k in l:
    b=k.copy()
    b.sort()
    if k==b or k==b[::-1]:
        s+=1
print(s)