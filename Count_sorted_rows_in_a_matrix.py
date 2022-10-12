n,m=map(int,input().split())
c=0
for i in range(n):
    l=list(map(int,input().split()))
    s=sorted(l)
    if l==s or l==s[::-1]:
        c+=1
print(c)