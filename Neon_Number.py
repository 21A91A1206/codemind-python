n=int(input())
sq=n*n
temp=n
Sum=0
while sq :
    rem=sq%10
    Sum=Sum+rem
    sq=sq//10
if(Sum==temp):
    print('Neon Number')
else:
    print("Not Neon Number")