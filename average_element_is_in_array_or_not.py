n=int(input())
a=list(map(int,input().split()))
b=0
for i in a:
    b=(b+i)
avg=b//n
if avg in a:
    print("True")
else:
    print("False")