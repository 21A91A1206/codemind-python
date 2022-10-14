s=input().lower().replace(' ','')
C=0
for i in s:
    if s.count(i)==1:
        C+=1
print(C)
        