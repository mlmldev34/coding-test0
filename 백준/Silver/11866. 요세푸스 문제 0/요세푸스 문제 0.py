n,k=map(int,input().split())
c=k
arr=[i+1 for i in range(n)]
brr=[]
for i in range(n):
    for j in range(1,n):
        if k-len(arr)>0:
            k-=len(arr)
        else:
            break
    if k-len(arr)>0:
        k-=len(arr)
    brr.append(arr[k-1])
    arr.pop(k-1)
    k+=c
    k-=1

print(str(brr).replace('[','<').replace(']','>'))