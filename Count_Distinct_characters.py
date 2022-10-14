s=input().lower().replace(' ','')
a=[]
for i in s:
    if i not in a:
        a.append(i)
print(len(a))