n=int(input())
Sum=0
mult=1
while n :
    rem=n%10
    Sum=Sum+rem
    mult=mult*rem
    n=n//10
if(Sum==mult):
    print("Spy Number")
else:
    print("Not Spy Number")