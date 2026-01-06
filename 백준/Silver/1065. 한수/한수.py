n=int(input())
r = 0

for i in range(1, n+1):
    a = list(map(int, list(str(i))))
    if(len(a)>2):
        if(len(a)%2):
            if(a[0]+a[-1]==a[len(a)//2]*2):
                r+=1
        else:
            if(a[0]+a[-1]==a[len(a)//2]+a[len(a)//2-1]):
                r+=1
    else:
        r+=1
print(r)