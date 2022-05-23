s=int(input())
while s:
    n=int(input())
    t=n
    rev=0
    while n:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if t==rev:
        print('True')
    else:
        print("False")
    s-=1