n=int(input())
a=int(-1+(1+8*(n-1))**0.5)//2+1
c=n-a*(a-1)//2
i,j=0,0

if a%2==0:
    i=0
    j=a+1
else:
    i=a+1
    j=0

for _ in range(c):
    if a%2==0:
        i+=1
        j-=1
    else:
        i-=1
        j+=1
print(f'{i}/{j}')