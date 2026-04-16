n,m=map(int,input().split())
arr=[]
brr=[]
crr=[0]*m
drr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    brr = list(map(int,input().split()))
    for j in range(m):
        crr[j] = arr[i][j] + brr[j]
    print(' '.join(map(str,crr)))