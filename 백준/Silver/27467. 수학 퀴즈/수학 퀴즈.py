n=int(input())
arr=list(map(int, input().split()))
r1=0
r2=0
for i in arr:
    if i%3==0:
        r1+=1
    elif (i-1)%3==0:
        r2+=1
    elif (i-2)%3==0:
        r1-=1
        r2-=1
print(f'{r2:.9f}', f'{r1:.9f}')