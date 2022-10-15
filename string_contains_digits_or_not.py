n=int(input())
for j in range(n):
    m=input()
    c=0
    for i in m:
        if i in "1234567890":
            c=c+1
    if(c>0):
        print("Yes")
    else:
        print("No")