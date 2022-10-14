l=input().lower().split()
m=input().lower().split()
a=[]
for i in l:
    if i in m:
        a.append(i)
for i in m:
    if i in a:
        print(i,end=' ')