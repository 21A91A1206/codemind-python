s=input()
sum=0
for i in s:
    for j in range(1,11):
        if i==str(j):
            sum=sum+int(i)
print(sum)