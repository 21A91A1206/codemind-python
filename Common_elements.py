a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
o=[]
for i in l:
    if i in m:
        if i not in o:
            o.append(i)
print(*o)
        

