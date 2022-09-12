a,b=map(int,input().split())
l=list(map(int,input().split()))
ll=list(map(int,input().split()))
c=[]
for i in l:
    if i in ll:
        if i not in c:
            c.append(i)
print(*c)