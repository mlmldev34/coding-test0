x,m=map(int,input().split())
t=x
arr=[x]
for i in range(m):
    for k in range(0,i+2,2):
        arr.append(arr[k]//2)
        if arr[k]/2>arr[k]//2:
            arr.append(arr[k]//2+1)
        else:
            arr.append(arr[k]//2)
        arr.pop(k)
    t+=sum(arr)
print(t)